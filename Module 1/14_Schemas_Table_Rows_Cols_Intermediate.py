'''
Q1. What is the goal of database normalization?
Ans:
Normalization removes repetition (redundancy) and ensures data is stored in the right tables so updates stay consistent.
'''
# Example:
# Avoid storing "Class-8" repeatedly in every student row.

'''

Q2. Why do we split data into multiple related tables?
Ans:
To reduce duplication and avoid update problems. Each table holds one type of information.
'''
# Example:
# Students table stores student info; Classes table stores class info.

'''

Q3. What is a functional dependency?
Ans:
A functional dependency means one column uniquely determines another column.
'''
# Example:
# student_id → name  
# (If you know ID, you know the name)

'''

Q4. What is the role of a primary key in schema design?
Ans:
A primary key uniquely identifies each row and ensures no two rows are identical.
'''
# Example:
# student_id must be unique.

'''

Q5. What is a foreign key, and why is it important?
Ans:
A foreign key links one table to another and ensures the related value actually exists.
'''
# Example:
# Marks.student_id must match Students.id.

'''

Q6. What is a "constraint" in a database?
Ans:
A constraint is a rule applied to a column or table to ensure valid and consistent data.
'''
# Example:
# NOT NULL, UNIQUE, CHECK age >= 5.

'''

Q7. Why is 1st Normal Form (1NF) required?
Ans:
1NF ensures each column has atomic (single) values and no repeating groups.
'''
# Example:
# Wrong: phone = "9876, 1234"  
# Right: separate rows or separate table.

'''

Q8. How does 3rd Normal Form (3NF) improve schema quality?
Ans:
3NF removes columns that depend on other non-key columns, preventing indirect dependencies.
'''
# Example:
# Storing "city" and also storing "zipcode → city" causes duplication.
