from pulumi import ComponentResource, ResourceOptions
import pulumi_aws as aws


class ServiceArgs:
    def __init__(self, subscriptions: aws.sns.Topic, ):
        self.subscriptions = subscriptions


class Service(ComponentResource):

    def __init__(self, name: str, args: ServiceArgs, opts: ResourceOptions = None):
        super().__init__("custom:app:Service", name, {}, opts)

        child_opts = ResourceOptions(parent=self)

        someQueue = aws.sqs.Queue(name + "-queue")

        topic_subscription = aws.sns.TopicSubscription(
            name + "-topicSubscription",
            topic=args.subscriptions.arn,
            protocol="sqs",
            endpoint=someQueue.arn
            )
