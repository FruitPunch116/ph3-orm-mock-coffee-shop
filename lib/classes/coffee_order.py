from lib import CONN, CURSOR
from lib.classes.customer import Customer

class CoffeeOrder:

    def __init__(self, coffee_name, price, customer_id, id=None):
        self.coffee_name = coffee_name
        self.price = price
        self.customer_id = customer_id
        self.id = id

    def __repr__(self):
        return f"CoffeeOrder(id: {self.id}, coffee_name: {self.coffee_name}, price: {self.price}, customer_id: {self.customer_id})"

    # THIS METHOD WILL CREATE THE SQL TABLE #
    @classmethod
    def create_table(cls):

    # ADD YOUR CODE BELOW #
        sql = """CREATE TABLE IF NOT EXISTS coffee_orders (
            id INTEGER PRIMARY KEY,
            coffee_name TEXT,
            price INTEGER,
            customer_id NUMBER
        )"""

        CURSOR.execute(sql)
        # CONN.commit()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if (type(value) == int or float) and value > 0:
            self._price = value
        else:
            raise ValueError('Price must be a number greater than zero')

    def create (self):
        # pass
        sql = """INSERT INTO coffee_orders (coffee_name, price, customer_id) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, [self.coffee_name, self.price, self.customer_id])
        CONN.commit()

        self.id = CURSOR.lastrowid

    def delete (self):
        # pass
        sql = """DELETE FROM coffee_orders WHERE id = ?"""
    
        CURSOR.execute(sql, [self.id])
        CONN.commit()

        self.id = None

    @classmethod
    def query_all (cls):
        # pass
        sql = """SELECT * FROM coffee_orders"""

        rows = CURSOR.execute(sql).fetchall()
        return [CoffeeOrder(row[1], row[2], row[3], row[0]) for row in rows]

    @classmethod
    def query_by_id(cls, id):
        sql = """SELECT * FROM coffee_orders WHERE id = ?"""

        row = CURSOR.execute(sql, [id]).fetchone()
        if row :
            return CoffeeOrder(row[1], row[2], row[3], row[0])
        else:
            return "Not valid order id, try again please"

    @property
    def customer(self):

        # Alternative
        # sql = """SELECT customer.id, customer.name FROM coffee_orders
        # LEFt JOIN customers ON coffee_orders.customer_id = customer.id
        # WHERE id = ?""""

        sql = """SELECT * FROM customers WHERE id = ?""" 

        row = CURSOR.execute(sql, [self.customer_id]).fetchone()

        if row :
            #Foreign key
            return Customer(row[1], row[0])
        else:
            return "Not valid user id, try again please"

    @customer.setter
    def customer(self, value):
        if isinstance (value, Customer):
            self.customer_id = value.id
        else:
            raise ValueError("Customerf must be of type Customer")