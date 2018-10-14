# Learn Alembic

## Getting Started

### Start a postgres container manually
`docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres`

## TODO

1. Write some code to setup an environment
  * create a docker alpine-postgres container 
  * create 2 databases in it
  * create a user and a table with some rows in one
  
2. Write some code to migrate the table definition from dev to prd

3. write code to migrate new col, and new index, from dev to prd

4. write code to remove column from prd


3. Write code to migrate user from dev to prd

4. Write code to migrate new privs on user from dev to prod

5. write code to remove privs from user in prd when not in dev