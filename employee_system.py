from database import Database
from employee import Employee


class EmployeeSystem:
    def __init__(self):
        self.employees = []
        self.database = Database()

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def add_employee_by_details(self, name, surname, salary, department):
        self.database.insert_employee(name, surname, salary, department)

    def get_employee_by_id(self, id):
        self.database.get_employee_by_id(id)

    def delete(self, id):
        self.database.delete_employee_by_id(id)

    def update_employee(self, id, name, surname, salary, department):
        self.database.update_employee(id, name, surname, salary, department)

    def delete_employee_by_details(self, name, surname, salary, department):
        for employee in self.employees:
            if employee.name == name and employee.surname == surname and employee.salary == salary and employee.department == department:
                self.employees.remove(employee)

    def search_by_name_surname(self, name, surname):
        emps = []
        for employee in self.employees:
            if employee.name == name and employee.surname == surname:
                emps.append(employee)
        return emps

    def search_by_salary(self, salary):
        em = []
        for employee in self.employees:
            if employee.salary == salary:
                em.append(employee)
        return em

    def search_by_department(self, department):
        emp = []
        for employee in self.employees:
            if employee.department == department:
                emp.append(employee)
        return emp
