# from .db_client import DBClient
from alembic.setup_env import Env


class TableMigration:

    def __init__(self):
        self.setup = Env()

    def setup_table(self):
        """
        Cleanup the db,
        Create the table in dev
        :return:
        """

        self.setup.create_basic_table_in_dev()
        self.setup.insert_random_records_into_dev()


def main():
    example = TableMigration()
    example.setup_table()


if __name__ == "__main__":
    main()
