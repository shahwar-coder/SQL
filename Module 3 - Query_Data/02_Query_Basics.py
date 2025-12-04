'''
====================  SQL QUERY — QUESTION SET (Concept Summary)  ====================

Since you provided a **Concept Summary**, this is CASE 2.
→ So here are **5 total Q/A**, progressing Easy → Medium → Deeper.

============================================================
Q1. What is an SQL query?   (Easy)
Ans:
An SQL query is a command you write to ask the database to do something.
It can show data, add data, update it, or delete it.

# Example:
# SELECT * FROM Students;   → "Show all students"

============================================================
Q2. Why do we use SQL queries instead of manual searching?   (Easy)
Ans:
Because SQL queries are fast.  
The database can find the exact data in seconds, even if the table has millions of rows.

# Example:
# Manually searching 10,000 students is slow → SQL does it instantly.

============================================================
Q3. Which SQL command is used to read data, and why?   (Beginner)
Ans:
The SELECT command is used to read data.
It does not change anything — it only fetches and shows results.

# Example:
# SELECT name, marks FROM Students WHERE marks > 90;

============================================================
Q4. What is the difference between INSERT, UPDATE, and DELETE?   (Beginner)
Ans:
• INSERT → adds a new row  
• UPDATE → changes an existing row  
• DELETE → removes a row

# Example:
# INSERT INTO Students VALUES (1, 'Aisha', 88);
# UPDATE Students SET marks = 95 WHERE id = 1;
# DELETE FROM Students WHERE id = 1;

============================================================
Q5. Why must we use WHERE in UPDATE and DELETE queries?   (Deeper)
Ans:
Because without WHERE, the command affects **every row** in the table.
WHERE limits the action to a specific row.

# Example:
# UPDATE Students SET marks = 0;         → ❌ changes ALL marks to 0
# UPDATE Students SET marks = 0 WHERE id = 5;   → ✔ only student with id=5

============================================================

Do you want more questions?
'''
