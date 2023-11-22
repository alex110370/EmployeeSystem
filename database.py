import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect('employee_system.db')
        self.cursor = self.connection.cursor()
        # self.cursor.execute('''CREATE TABLE employees (
        # id INTEGER PRIMARY KEY AUTOINCREMENT,
        # name TEXT NOT NULL,
        # surname TEXT NOT NULL,
        # department INTEGER NOT NULL,
        # salary INTEGER NOT NULL
        #  );''')

    def insert_employee(self, name, surname, department, salary):
        self.cursor.execute('''INSERT INTO employees(name, surname, department, salary) VALUES(?, ?, ?, ?)''',
                            (name, surname, department, salary))
        self.connection.commit()

    def get_employees(self):
        self.cursor.execute('''SELECT * FROM employees''')
        return self.cursor.fetchall()

    def get_employee_by_id(self, id):
        self.cursor.execute('''SELECT * FROM employees WHERE id = ?''', (id,))
        return self.cursor.fetchall()
    def update_employee(self, id, name, surname, department, salary):
        self.cursor.execute('''UPDATE employees SET name = ?, surname = ?, department = ?, salary = ? WHERE id = ? ''',
                            (name, surname, department, salary, id))
        self.connection.commit()

    def delete_employee_by_id(self, id):
        self.cursor.execute('''DELETE FROM employees WHERE id = ?''', (id,))
        self.connection.commit()