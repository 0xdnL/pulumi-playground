import pulumi
import pulumi_aws as aws


from service import Service, ServiceArgs

config = pulumi.Config()

myServices = [
    # "apple",
    # "banana",
    "cherry"
]

for svc in myServices:
    someTopic   = aws.sns.Topic(
        "pulumi-svc-" + svc + "-topic",
        tags={'project': pulumi.get_project(), 'stack': pulumi.get_stack(), 'managedBy': 'pulumi'}
        )

    someBucket  = aws.s3.Bucket(
        'pulumi-svc-' + svc + "-bucket",
        force_destroy=True,
        tags={'project': pulumi.get_project(), 'stack': pulumi.get_stack(), 'managedBy': 'pulumi'}
        )

    someService = Service("pulumi-svc-" + svc, ServiceArgs(subscriptions=someTopic))

    pulumi.export('someTopic', someTopic.name)
    pulumi.export('someBucket', someBucket.arn)
