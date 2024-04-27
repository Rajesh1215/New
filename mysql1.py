import mysql.connector

class Student:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
        """)
        self.connection.commit()

    def add_student(self, name, age):
        self.cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
        self.connection.commit()

    def get_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def update_student(self, student_id, name, age):
        self.cursor.execute("UPDATE students SET name = %s, age = %s WHERE id = %s", (name, age, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        self.connection.commit()

# Connect to the database
connection = mysql.connector.connect(host="localhost", port=5000, user="root", password="", database="mini")

# Create an instance of the Student class
student_manager = Student(connection)

# Create the table if it doesn't exist
student_manager.create_table()

# Add a new student
student_manager.add_student("John Doe", 25)

# Get all students
students = student_manager.get_students()
print("Students:")
for student in students:
    print(student)

# Update a student
student_manager.update_student(5, "Jane Doe dev", 26)
students = student_manager.get_students()

print("Students:")
for student in students:
    print(student)


# # Delete a student
# student_manager.delete_student(1)

# # Get all students after deletion
# students = student_manager.get_students()
# print("Students after deletion:")
# for student in students:
#     print(student)

# Close the connection
connection.close()
