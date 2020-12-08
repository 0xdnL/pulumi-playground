"""A Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import pulumi_terraform as terraform

# Reference the Terraform state file:
lambda_state = terraform.state.RemoteStateReference(
    resource_name='lambda',
    backend_type='local',
    args=terraform.state.LocalBackendArgs(path='./example.terraform.tfstate'))

aws_lambda = lambda_state.get_output("aws_lambda_function_results_updates_lambda")

print(aws_lambda.value.arn)
print(aws_lambda.value.arn.tags)

# Read the VPC and subnet IDs into variables:
# vpc_id = network_state.get_output('vpc_id')
# public_subnet_ids = network_state.get_output('public_subnet_ids')
#
# # Now spin up servers in the first two subnets:
# for i in range(2):
#     aws.ec2.Instance(f'instance-{i}',
#         ami='ami-7172b611',
#         instance_type='t2.medium',
#         subnet_id=public_subnet_ids[i])
