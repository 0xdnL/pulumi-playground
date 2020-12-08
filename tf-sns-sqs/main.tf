terraform {
  backend "local" {
  }
  required_providers {
    aws = {
      version = ">= 3.0"
      source  = "hashicorp/aws"
    }
  }
}


provider "aws" {
  region = "eu-central-1"
}

data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda/example.js"
  output_path = "${path.module}/lambda/example.zip"
}

resource "aws_sns_topic" "results_updates" {
  name = "results-updates-topic"
}

resource "aws_sqs_queue" "results_updates_queue" {
  name = "results-updates-queue"
  redrive_policy = jsonencode({
    "deadLetterTargetArn" : aws_sqs_queue.results_updates_dl_queue.arn,
    "maxReceiveCount" : 5
  })
  visibility_timeout_seconds = 300

  tags = {
    project = "pulumi-playground"
  }
}


resource "aws_sqs_queue" "results_updates_dl_queue" {
  name = "results-updates-dl-queue"
}

resource "aws_sqs_queue_policy" "results_updates_queue_policy" {
  queue_url = aws_sqs_queue.results_updates_queue.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Id" : "sqspolicy",
    "Statement" : [
      {
        "Sid" : "First",
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : "sqs:SendMessage",
        "Resource" : aws_sqs_queue.results_updates_queue.arn,
        "Condition" : {
          "ArnEquals" : {
            "aws:SourceArn" : aws_sns_topic.results_updates.arn
          }
        }
      }
    ]
  })
}

resource "aws_sns_topic_subscription" "results_updates_sqs_target" {
  topic_arn = aws_sns_topic.results_updates.arn
  endpoint  = aws_sqs_queue.results_updates_queue.arn
  protocol  = "sqs"
}

resource "aws_iam_role" "lambda_role" {
  name = "LambdaRole"
  assume_role_policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : "sts:AssumeRole",
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "lambda.amazonaws.com"
        }
      }
    ]
  })
  tags = {
    project = "pulumi-playground"
  }
}

resource "aws_iam_role_policy" "lambda_role_logs_policy" {
  name = "LambdaRolePolicy"
  role = aws_iam_role.lambda_role.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        "Effect" : "Allow",
        "Resource" : "*"
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_role_sqs_policy" {
  name = "AllowSQSPermissions"
  role = aws_iam_role.lambda_role.id
  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Action" : [
          "sqs:ChangeMessageVisibility",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes",
          "sqs:ReceiveMessage"
        ],
        "Effect" : "Allow",
        "Resource" : "*"
      }
    ]
  })
}

resource "aws_lambda_function" "results_updates_lambda" {
  function_name    = "hello_world_example"
  role             = aws_iam_role.lambda_role.arn
  handler          = "example.handler"
  runtime          = "nodejs12.x"
  filename         = "${path.module}/lambda/example.zip"
  source_code_hash = data.archive_file.lambda_zip.output_base64sha256

  environment {
    variables = {
      foo = "bar"
    }
  }
  tags = {
    project = "pulumi-playground"
  }
}

resource "aws_lambda_event_source_mapping" "results_updates_lambda_event_source" {
  event_source_arn = aws_sqs_queue.results_updates_queue.arn
  enabled          = true
  function_name    = aws_lambda_function.results_updates_lambda.arn
  batch_size       = 1
}

output aws_lambda_function_results_updates_lambda {
  value       = aws_lambda_function.results_updates_lambda
  description = "The AWS SQS name of the digital survey answers command topic."
}
