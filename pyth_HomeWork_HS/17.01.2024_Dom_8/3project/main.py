
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
