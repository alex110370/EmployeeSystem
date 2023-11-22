from employee import Employee
from employee_system import EmployeeSystem

employee_system = EmployeeSystem()
emp = Employee('Иван', 'Петров', 230, 'Розница')
employee_system.add_employee(emp)
print(employee_system.employees)
# employee_system.delete_employee_by_details('Иван', 'Петров', 230, 'Розница')
print(employee_system.employees)
employee_system.add_employee_by_details('Степан', 'Иванов', 250, 'Опт')
employee_system.add_employee_by_details('Петр', 'Иванов', 250, 'Опт')
employee_system.add_employee_by_details('Алексей', 'Иванов', 250, 'Опт')
employee_system.add_employee_by_details('Степан', 'Иванов', 250, 'Опт')
print(employee_system.search_by_name_surname('Степан', 'Иванов'))
print(employee_system.search_by_salary(250))
print(employee_system.search_by_department('Опт'))
