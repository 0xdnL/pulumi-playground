# aws js lambda

## prerequesites
- `npm` installed

## setup
```sh
mkdir aws-js-lambda && cd $_

pulumi new hello-aws-javascript --name aws-js-lambda


pulumi up

curl $(pulumi stack output url)

pulumi destroy

pulumi stack rm STACKNAME
```

## see also
- [pulumi.com/docs/tutorials/aws/rest-api/](https://www.pulumi.com/docs/tutorials/aws/rest-api/)
