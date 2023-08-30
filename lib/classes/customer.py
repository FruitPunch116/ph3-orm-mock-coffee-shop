from lib import CONN, CURSOR

class Customer:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name})"


    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        """

        CURSOR.execute(sql)

    def create(self):
        sql = """INSERT INTO customers (name) VALUES (?)
        """

        CURSOR.execute(sql, [self.name])
        CONN.commit()