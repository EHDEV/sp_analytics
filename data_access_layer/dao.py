from config import database_config
import psycopg2
import psycopg2.extras as pse

class Dao:

    def __init__(self):

        self.conn = psycopg2.connect (
            database=database_config["DATABASE"],
            host=database_config["HOST"],
            port=database_config["PORT"],
            user=database_config["USER"],
            password=database_config["PASSWORD"]
        )

        self.cursor = self.conn.cursor(cursor_factory=pse.DictCursor)


    def query(self, q):

        self.cursor.execute(q)
        data = self.cursor.fetchall()
        return data
