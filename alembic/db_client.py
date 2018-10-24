import psycopg2


class DBClient:

    def __init__(self):
        self.conn = None

    def setup_connection(self, db_name):
        self.conn = psycopg2.connect(dbname=db_name, user="postgres", host='localhost', password="pgpass", port=5432)
        self.conn.set_session(autocommit=True)
        print('successfully connected to {}'.format(db_name))

    def test_connection(self):
        cursor = self.conn.cursor()

        cursor.execute('select count (*) from pg_stat_activity')

        print('If Im working, then there are {} connections to the db, if not, '
              'you saw an exception and error'.format(cursor.fetchone()[0]))

    def exec_select_sql(self, sql):
        cursor = self.conn.cursor()

        cursor.execute(sql)
        return cursor.fetchall()

    def exec_ddl(self, sql, params):
        """
        Do some ddl, like create a table or some such
        :return:
        """

        cursor = self.conn.cursor()
        print(cursor.mogrify(sql, params))
        cursor.execute(sql, params)



# db = DBClient()
# db.setup_connection('dev')
# db.test_connection()
# # db.create_learning_databases()
# db.exec_ddl('create table public.x ( col1 text, col2 integer)')
