# In a folder called project create three files:person.py, employee.py, and teacher.py.
# In each file, create its corresponding class -person,employee, and teacher:
# • person with a single method sleep() that returns: "sleeping..."
# • employee with a single method get_fired()that returns: "fired..."
# • teacher with a single method teach() that returns: "teaching..."
# Teacher should inherit from person and employee

# teacher.py
from person import Person
from employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

from person import Person
from employee import Employee
from teacher import Teacher

# Creating instances
person_instance = Person()
employee_instance = Employee()
teacher_instance = Teacher()

# Calling methods
print(person_instance.sleep())          # Output: sleeping...
print(employee_instance.get_fired())    # Output: fired...
print(teacher_instance.sleep())          # Output: sleeping... (inherited from Person)
print(teacher_instance.get_fired())     # Output: fired... (inherited from Employee)
print(teacher_instance.teach())         # Output: teaching...
