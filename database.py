import os
import psycopg2
from psycopg2.extras import DictCursor
from typing import List, Dict

class PostgresDatabase:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv("DATABASE_NAME"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD"),
            host=os.getenv("DATABASE_HOST"),
            port=5432
        )
        self.cur = self.conn.cursor(cursor_factory=DictCursor)

    def query(self, query: str, params: Dict = None) -> List[Dict]:
        if params is None:
            self.cur.execute(query)
        else:
            self.cur.execute(query, params)
        results = self.cur.fetchone()
        return results[0]

    def close(self):
        self.cur.close()
        self.conn.close()
