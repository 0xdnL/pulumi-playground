# pulumi playground

> pulumi is an infrastructure-as-code tool that creates, deploys and manages cloud infrastructure

## prerequesites
- `aws` cli installed 
- `puliumi` installed e.g. `brew install pulumi`
- language runtime installed e.g. typescript, javascript, python, go, c#
- cloud credentials setup e.g. `$HOME/.aws/`
- `pulumi config set aws:profile PROFILE_NAME`

## setup
```sh
pulumi gen-completion bash > /usr/local/etc/bash_completion.d/pulumi
```

```sh
export AWS_PROFILE=PROFILE_NAME

pulumi config set aws:profile PROFILE_NAME    
# Enter your access token from https://app.pulumi.com/account/tokens
#     or hit <ENTER> to log in using your browser                   :
# We've launched your web browser to complete the login process.
#
# Waiting for login to complete...
```

## first project
```sh
$ pulumi new aws-go --dir ./aws-go

This command will walk you through creating a new Pulumi project.
..
project name: (aws-go)
project description: (A minimal AWS Go Pulumi program)
Created project 'aws-go'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev) ec/experimental
Sorry, 'ec/experimental' is not a valid stack name. invalid stack owner.
stack name: (dev) experimental
Created stack 'experimental'
aws:region: The AWS region to deploy into: (us-east-1) eu-central-1
Installing dependencies...
```


## first steps
```sh
cd ./aws-go
export AWS_PROFILE=PROFILE_NAME

puliumi preview

pulumi up   # evaluate program and determine resources updates to make, runs interactively

aws s3api list-buckets | jq -r '.Buckets[].Name'

pulumi stack ls
pulumi stack output bucketName      # print out the name of bucket

aws s3 ls $(pulumi stack output bucketName)
```
