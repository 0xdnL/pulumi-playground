# importing existing cloud infrastructure to pulumi


## usage
```sh
export AWS_PROFILE=

pulumi new aws-python      # select aws-python template..

aws s3api list-buckets | jq -r '.Buckets[].Name'

pulumi import aws:s3/bucket:Bucket PULUMI_NAME INFRA_ID

pbpaste >> __main__.py
```

## batch import

```sh
pulumi import -f resources.json
```

```json
{
	"resources": [{
			"type": "aws:ec2/vpc:Vpc",
			"name": "application-vpc",
			"id": "vpc-0ad77710973388316"
		},
		{
			"type": "aws:ec2/subnet:Subnet",
			"name": "public-1",
			"id": "subnet-0fb5fdff92b9e5a3b"
		},
		{
			"type": "aws:ec2/subnet:Subnet",
			"name": "private-1",
			"id": "subnet-0a39d25dd9f7b7808"
		}
	]
}
```

## remove from state
```sh
pulumi stack --show-urns      # similar to terraform state list

pulumi state delete URN [flags]
```

## see also
- [pulumi.com/blog/pulumi-import-generate-iac-for-existing-cloud-resources](https://www.pulumi.com/blog/pulumi-import-generate-iac-for-existing-cloud-resources/#importing-an-s3-bucket)
