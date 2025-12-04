'''
============================================================
Q1. What does the SELECT command do in SQL?
Ans:
SELECT is used to **show data** from a table.  
It’s like asking the database a question.

Example:
SELECT * FROM Students;   # shows all data

------------------------------------------------------------

Q2. What does the * symbol mean in a SELECT query?
Ans:
It means **select everything** (all columns).

Example:
SELECT * FROM Books;   # title, author, price… everything

------------------------------------------------------------

Q3. How do you select only some columns from a table?
Ans:
Write the column names after SELECT.

Example:
SELECT name, marks FROM Students;   # shows only these two columns

------------------------------------------------------------

Q4. How do you select rows that satisfy a condition?
Ans:
Use the **WHERE** clause to filter rows.

Example:
SELECT name FROM Students WHERE marks > 80;  
# shows only students who scored above 80

------------------------------------------------------------

Q5. What will this SQL query return?
    SELECT name, age FROM Students;
Ans:
It will show **only the name and age columns** of all students.

Example output:
Aisha | 14
Rohan | 15
Jiya  | 14

============================================================
'''
