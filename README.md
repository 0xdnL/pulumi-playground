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
- language runtime installed e.g. typescript, javascript, python, go, c#
- cloud credentials setup e.g. `$HOME/.aws/`
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

## see also
- [pulumi.com/docs/get-started/aws](https://www.pulumi.com/docs/get-started/aws/begin/)
- [pulumi.com/docs/tutorials/aws/rest-api/](https://www.pulumi.com/docs/tutorials/aws/rest-api/)
- [youtube.com/c/PulumiTV/videos](https://www.youtube.com/c/PulumiTV/videos)
- [Pulumi Crosswalk for AWS](https://www.pulumi.com/docs/guides/crosswalk/aws/)
