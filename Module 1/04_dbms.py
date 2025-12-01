'''
Q1. What does DBMS stand for?
Ans:
DBMS stands for Database Management System.
'''
# Example: MySQL is a DBMS.

'''
Q2. What is the main purpose of a DBMS?
Ans:
To store and manage data in an organized way.
'''
# Example: A school stores student details in a DBMS.

'''
Q3. How does a DBMS store data?
Ans:
It stores data in tables made of rows and columns.
'''
# Example: A table of students with RollNo, Name, Marks.

'''
Q4. Why is a DBMS better than keeping data on paper?
Ans:
Because it is faster, safer, and easier to search or update data.
'''
# Example: Finding a student’s marks instantly.

'''
Q5. What is an example of data that a DBMS can store?
Ans:
Student records, teacher information, fees, books, etc.
'''
# Example: Roll number → 12, Name → Aisha.

'''
Q6. Name any one DBMS.
Ans:
MySQL, Oracle, PostgreSQL, or SQLite.
'''
# Example: WhatsApp uses SQLite internally.

'''
Q7. What is a 'table' in DBMS?
Ans:
A table is a collection of related data arranged in rows and columns.
'''
# Example: A Marks table with columns (RollNo, Subject, Marks).


'''SET-2
Q1. What is the difference between a Database and a DBMS?
Ans:
A database stores the actual data, while a DBMS is the software used to manage that data.
'''
# Example:
# Database = tables with student records
# DBMS = MySQL, which manages those tables

'''

Q2. What is a schema in DBMS?
Ans:
A schema describes the structure of the database—tables, columns, and how they relate.
'''
# Example:
# Students table: (rollno INT, name VARCHAR, class INT)

'''

Q3. What is a table in DBMS?
Ans:
A table stores data in rows and columns, where each row is a record and each column is a field.
'''
# Example:
# student(rollno, name, class)

'''

Q4. What is a primary key?
Ans:
A primary key is a column that uniquely identifies each row in a table.
'''
# Example:
# Roll number in the Students table.

'''

Q5. Why must a primary key be unique and not null?
Ans:
Because it identifies a row, so it cannot repeat and cannot be empty.
'''
# Example:
# Two students cannot have the same roll number.

'''

Q6. What happens if you try to insert duplicate primary keys?
Ans:
The DBMS will reject the insertion because it violates uniqueness.
'''
# Example:
# Adding rollno = 5 again will cause an error.

'''

Q7. Why do we use multiple tables instead of one big table?
Ans:
To avoid repetition, keep data organized, and make updates easier.
'''
# Example:
# Students table and Subjects table instead of mixing everything together.
