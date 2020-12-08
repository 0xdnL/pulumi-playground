"""An AWS Python Pulumi program"""

# import pulumi
# from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
# bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)

import pulumi
import pulumi_aws as aws

foo_bucket = aws.s3.Bucket("fooBucket",
    acl="private",
    bucket="someBucket",
    cors_rules=[aws.s3.BucketCorsRuleArgs(
        allowed_methods=["GET"],
        allowed_origins=["*"],
    )],
    force_destroy=False,
    server_side_encryption_configuration=aws.s3.BucketServerSideEncryptionConfigurationArgs(
        rule=aws.s3.BucketServerSideEncryptionConfigurationRuleArgs(
            apply_server_side_encryption_by_default=aws.s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
                kms_master_key_id="arn:aws:kms:REGION:ID:key/KEY_ID",
                sse_algorithm="aws:kms",
            ),
        ),
    ),
    tags={
        "managed-by": "terraform",
        "project": "someBucket",
    },
    opts=pulumi.ResourceOptions(protect=True))
