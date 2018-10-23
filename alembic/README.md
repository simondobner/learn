# Learn Alembic

## Getting Started

### Start a postgres container manually
`docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`  
or, if you've already created and run it once,  
`$ docker start some-postgres`
## TODO

1. Write some code to setup an environment
  * DONE - create a docker alpine-postgres container 
  * DONE - via db_client.create_learning_databases (dev, prd): create 2 databases in it
  
  * create a  table in dev
  
  * insert a bunch of rows into the table in dev.
  
2. Write some code to migrate the table definition from dev to prd

3. write code to migrate new col, and new index, from dev to prd

4. write code to remove column from prd


3. Write code to migrate user from dev to prd

4. Write code to migrate new privs on user from dev to prod

5. write code to remove privs from user in prd when not in dev