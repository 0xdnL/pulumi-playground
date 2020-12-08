# pulumi playground

> pulumi is an infrastructure-as-code tool that creates, deploys and manages cloud infrastructure

- instead of yml or a sdl, `pulumi` uses existing, programming languages and their native tools, libraries, and package managers
- `pulumi up` executes program and determines the desired infrastructure state for all resources declared
- pulumi programs are written in general-purpose programming languages

- Pulumi programs are structured as projects and stacks
  - `Program` a collection of files written in chosen programming language
  - `Project` a directory containing a program, with metadata, so Pulumi knows how to run it
  - `Stack` an instance of your project, each often corresponding to a different cloud environment

## prerequesites
- `puliumi` installed e.g. `brew install pulumi`
- `tf2pulumi` installed e.g. `brew install pulumi/tap/tf2pulumi`
- language runtime installed e.g. `node`, `python`, `go`
- aws profile and credentials present at `$HOME/.aws/`
- (optional) `aws` cli installed
- (optional) `curl` cli installed

## setup
```sh
pulumi gen-completion bash > /usr/local/etc/bash_completion.d/pulumi

export AWS_PROFILE=PROFILE_NAME

pulumi config set aws:profile PROFILE_NAME    # interactively auth pulumi
```

## first steps
```sh
cd ./aws-go
export AWS_PROFILE=PROFILE_NAME

pulumi new <CLOUD>-<LANG> --name PROJECT_NAME

pulumi new aws-go --dir ./aws-go      # interactively setup project, stack and dependencies

puliumi preview

pulumi up   # evaluate program and determine resources updates to make, runs interactively

aws s3api list-buckets | jq -r '.Buckets[].Name'

pulumi stack ls

pulumi stack output bucketName      # print out the name of bucket

aws s3 ls $(pulumi stack output bucketName)

curl $(pulumi stack output bucketEndpoint)
```

## cleanup
```sh
cd ./aws-go && pulumi destroy

# history and configuration associated with the stack are still maintained, total cleanup !
pulumi stack rm STACK_NAME
```

## from terraform to pulumi
if existing infrastructure was provisioned with Terraform, there are a number of options that will help you adopt Pulumi
- Coexist with resources provisioned by Terraform by referencing a `.tfstate`
- Import existing resources into Pulumi in the usual way or using the `tf2pulumi` to adopt all resources from an existing `.tfstate`
- converting HCL to Pulumi code using `tf2pulumi`

## see also
- [pulumi.com/docs/get-started/aws](https://www.pulumi.com/docs/get-started/aws/begin/)
- [pulumi.com/docs/tutorials/aws/rest-api/](https://www.pulumi.com/docs/tutorials/aws/rest-api/)
- [youtube.com/c/PulumiTV/videos](https://www.youtube.com/c/PulumiTV/videos)
- [Pulumi Crosswalk for AWS](https://www.pulumi.com/docs/guides/crosswalk/aws/)
- [pulumi.com/docs/guides/adopting/from_terraform/](https://www.pulumi.com/docs/guides/adopting/from_terraform/)
- [github.com/pulumi/tf2pulumi#building-and-installation](https://github.com/pulumi/tf2pulumi#building-and-installation)
- [pulumi.com/tf2pulumi/](https://www.pulumi.com/tf2pulumi/)
