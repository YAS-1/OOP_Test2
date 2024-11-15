
# Function to add a student to the list
def add_student(student_list, student_id, name, age, course):

# Check if the student ID already exists
    if any(student['id'] == student_id for student in student_list):
        print("Error: Student ID already exists!")
        return
# Create a new student dictionary
    student = {
        'id': student_id,
        'name': name,
        'age': age,
        'course': course
    }
    student_list.append(student)# Add student to the list

# Function to find a student by their ID
def find_student(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            return student  # Return the found student
    print("Error: Student not found!") # Error message if not found
    return None

# Function to remove a student by their ID
def remove_student(student_list, student_id):
    for student in student_list:
        if student['id'] == student_id:
            student_list.remove(student)# Remove the student from the list
            return
    print("Error: Student not found!") # Error message if not found

# Base class for a person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"# String representation of the person

# Subclass for students
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)# Call the parent class constructor
        self.course = course

    def study(self):
        print(f"Student is studying {self.course}.")# Output statement for study action

class Instructor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)# Call the parent class constructor
        self.subject = subject

    def teach(self):
        print(f"Instructor is teaching {self.subject}.")# Output statement for teaching action

student = Student("Alice",20,"Math")
instructor = Instructor("Bob",35,"Physics")

student.study()
instructor.teach()


# Function to sort students
def sort_students(student_list, key_function):
    return sorted(student_list, key=key_function)

students = [
    {'id': 1, 'name': 'Lynn', 'age': 25, 'course': 'Civil'},
    {'id': 2, 'name': 'Tim', 'age': 19, 'course': 'Law'},
    {'id': 3, 'name': 'Pat', 'age': 32, 'course': 'Art'},
]

# Sorting by age
sortedby_age = sort_students(students, key_function=lambda x: x['age'])
print("Sorted by age:")
for student in sortedby_age:
    print(student)

# Sorting by name
sortedby_name = sort_students(students, key_function=lambda x: x['name'])
print("\nSorted by name:")
for student in sortedby_name:
    print(student)