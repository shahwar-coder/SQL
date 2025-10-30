'''
Q1. What is the difference between DDL and DML in SQL?  
Ans:  
✅ DDL → **Defines** the structure of the database (tables, columns).  
✅ DML → **Manipulates** the data stored inside the tables.  

🧩 Example:  
DDL → CREATE TABLE Students (...)  
DML → INSERT INTO Students VALUES (...);
'''
# Quick Demo Example:
DDL = "CREATE TABLE Students (id INT, name VARCHAR(50));"
DML = "INSERT INTO Students VALUES (1, 'Riya');"
print("DDL Example:", DDL)
print("DML Example:", DML)




'''
Q2. Which SQL commands are part of DDL?  
Ans:  
✅ CREATE, ALTER, DROP, TRUNCATE  
→ All are used to define or modify table structures.
'''



'''
Q3. Which SQL commands belong to DML?  
Ans:  
✅ SELECT, INSERT, UPDATE, DELETE  
→ All work with the data stored in the tables.
'''



'''
Q4. Can you use the WHERE clause with DDL commands?  
Ans:  
❌ No.  
DDL affects the **entire table**, not specific rows.
'''



'''
Q5. Can DML operations be rolled back?  
Ans:  
✅ Yes.  
DML changes (like INSERT, UPDATE, DELETE) can be undone with **ROLLBACK**.  
DDL changes **cannot** be undone.
'''



'''
Q6. Explain the main purpose of the CREATE and ALTER commands.  
Ans:  
✅ CREATE → Makes new database objects (tables, databases).  
✅ ALTER → Modifies existing ones (add, delete, or rename columns).  

🧩 Example:  
ALTER TABLE Students ADD age INT;
'''



'''
Q7. Which command will delete all records from a table but keep the table itself?  
Ans:  
✅ TRUNCATE  
🧩 Example: TRUNCATE TABLE Students;
'''



'''
Q8. Which command will completely remove the table structure from the database?  
Ans:  
✅ DROP  
🧩 Example: DROP TABLE Students;
'''



'''
Q9. Fill in the blanks:  
1️⃣ DDL defines ________.  
2️⃣ DML manipulates ________.  

Ans:  
✅ DDL → structure of the database  
✅ DML → data inside the database
'''



'''
💡 DDL vs DML Trick:

D → Define → DDL (CREATE, ALTER, DROP, TRUNCATE)  
M → Manipulate → DML (SELECT, INSERT, UPDATE, DELETE)

🧩 Example:
DDL → CREATE TABLE Employees (...)  
DML → UPDATE Employees SET salary = 50000 WHERE id = 3;
'''
