# LocalStack test project

## To start the openstack environment in docker, 

1. clone the repo
`$ git clone git@github.com:localstack/localstack.git` - you only need to do this once
( look for a copy in the PyCharmProjects dir

2. start the docker container
`TMPDIR=/private$TMPDIR docker-compose up`

Stop it later with `docker-compose down`

## Do some stuff


1. push a bunch of different messages ( have a set of attributes, and randomly assign one to each message)
2. get them back
3. attach a lambda to the SQS queue to write the message details to a file
4. make the lambda write them to a dynamodb
5. add another lambda to fan out the writes to different tables, based on message attributes.

