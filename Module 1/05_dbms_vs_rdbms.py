'''
Q1. What is a DBMS?
Ans:
A DBMS is software that helps store and manage data in tables.
'''
# Example: MySQL, Oracle

'''

Q2. What is an RDBMS?
Ans:
An RDBMS is a type of DBMS that stores data in tables that are linked (related) to each other.
'''
# Example: Students table linked to Marks table using roll number.

'''

Q3. What is the main difference between DBMS and RDBMS?
Ans:
DBMS stores data, but RDBMS also connects related data using keys.
'''
# Example: RDBMS can link a student to their marks.

'''

Q4. Which one uses relationships between tables?
Ans:
RDBMS uses relationships.
'''
# Example: Student → has many → Marks rows

'''

Q5. Does RDBMS always use tables?
Ans:
Yes, RDBMS stores all data in tables.
'''
# Example: Each table has rows & columns.

'''

Q6. Can DBMS be used on small systems like phones?
Ans:
Yes, DBMS can be simple and used on small devices.
'''
# Example: A basic file-based database.

'''

Q7. Which one is more powerful: DBMS or RDBMS?
Ans:
RDBMS is more powerful because it supports relations and rules.
'''
# Example: Foreign keys ensure data stays correct.


'''
DBMS                                RDBMS
-------------------          ----------------------------
Stores data only             Stores data + relations
Tables not linked            Tables linked by keys
No PK-FK enforcement         Strong rules (PK, FK, constraints)
Used for small systems       Used for large, reliable systems
'''
