'''
Q1. What does SQL stand for and what is it used for?  
Ans:  
✅ SQL → **Structured Query Language**.  
It is used to **store**, **retrieve**, **update**, and **manage** data in relational databases.  

🧩 Example:  
`SELECT * FROM students;` → retrieves all data from the table named *students*.
'''



'''
Q2. What kind of language is SQL — procedural or declarative?  
Ans:  
✅ Declarative.  
In SQL, you tell the database *what* result you want, not *how* to get it.
'''



'''
Q3. Name any two popular RDBMS that use SQL.  
Ans:  
✅ Examples: MySQL, PostgreSQL, Oracle, SQL Server.  
(All follow SQL standards but with slight differences.)
'''



'''
Q4. How is “LIMIT” in MySQL different from “TOP” in SQL Server?  
Ans:  
✅ Both control the number of rows returned,  
but syntax differs:  
🧩 MySQL → `SELECT * FROM table LIMIT 5;`  
🧩 SQL Server → `SELECT TOP 5 * FROM table;`
'''



'''
Q5. What are the four main operations SQL can perform on data?  
Ans:  
✅ INSERT → store new data  
✅ SELECT → retrieve data  
✅ UPDATE → change data  
✅ DELETE → remove data
'''



'''
Q6. Explain in your own words why SQL is called “Structured.”  
Ans:  
✅ Because it follows a **fixed, logical structure** — using clear keywords  
like SELECT, FROM, WHERE — to communicate with databases.
'''



'''
Q7. Which SQL statement is used to remove data from a table?  
Ans:  
✅ DELETE statement.  
🧩 Example: `DELETE FROM students WHERE marks < 35;`
'''



'''
Q8. Fill in the blank:  
SQL helps users ________ and ________ data in databases.  
Ans:  
✅ store, retrieve (also update, delete)
'''



'''
💡 SQL Quick Formula:

S → Store data (INSERT)  
Q → Query data (SELECT)  
L → Lend structure to updates (UPDATE, DELETE)

🧩 Example:
SELECT name FROM students WHERE grade = 'A';
'''
