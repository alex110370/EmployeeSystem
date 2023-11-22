class Employee:
    ID = 1

    def __init__(self, name, surname, salary, department):
        self.id = Employee.ID
        self.surname = surname
        self.salary = salary
        self.name = name
        self.department = department
        Employee.ID += 1

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Зарплата: {self.salary}\n" \
               f"Отдел: {self.department}\n"

    def __repr__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Зарплата: {self.salary}\n" \
               f"Отдел: {self.department}\n"
