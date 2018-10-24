import string

from alembic.db_client import DBClient
from random import randint, choice


class Env:
    def __init__(self):
        self.create_learning_databases()
        self.dev_db_conn = DBClient()
        self.dev_db_conn.setup_connection('dev')

        self.table_name = 'table_' + str(randint(1, 10000))
        print('the table in dev is called `{}`'.format(self.table_name))

    @staticmethod
    def create_learning_databases():
        """
        create a connection to the postgres database and Drop and recreate empty databases
        :return: None
        """
        pg_client = DBClient()
        pg_client.setup_connection('postgres')
        cursor = pg_client.conn.cursor()

        cursor.execute('drop database if exists prd')
        cursor.execute('create database prd')
        cursor.execute('drop database if exists dev')
        cursor.execute('create database dev')
        pg_client.conn.close()

    def create_basic_table_in_dev(self):
        """
        Create a table in dev
        
        :return: the name of the table it's created
        """
        dev_table_sql = "create table {} ( col1 text, col2 int, col3 timestamp )".format(self.table_name)

        self.dev_db_conn.exec_ddl(dev_table_sql, None)

    def insert_random_records_into_dev(self):
        "insert a bunch of records into "
        for x in range(randint(100, 1000)):
            sql = "insert into {} values (%s, %s, current_timestamp)".format(self.table_name)
            print(sql)
            self.dev_db_conn.exec_ddl(sql, [''.join([choice(string.ascii_lowercase) for i in range(15)]),
                                      randint(1, 10000)])
