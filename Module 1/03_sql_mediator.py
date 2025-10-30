'''
[ Your Computer ]   --(1) Querying: write SQL-->   [ SSMS (write SQL here) ]   --(2) Send query-->   [ Database (tables & data) ]
       ^                                                                                                                             |
       |                                                                                                                             v
       \----------------(4) Display results <---(3) Retrieve result <---------------------------------------------------------------/

'''

# ===============================================================================================

'''
Q1. What is SSMS and what is it used for?  
Ans:  
✅ SSMS → **SQL Server Management Studio**.  
It is a tool used to **write, send, and execute SQL queries** on a database.  

🧩 Example:  
You write `SELECT * FROM Students;` in SSMS →  
SSMS sends it to the database → database returns the results → SSMS displays them.
'''



'''
Q2. What is the first step in the SQL query flow?  
Ans:  
✅ You write the SQL query in SSMS.  
(Example: SELECT name FROM Students;)
'''



'''
Q3. What does SSMS do after you write a SQL query?  
Ans:  
✅ It sends the query to the **database** for processing.
'''



'''
Q4. What happens inside the database after SSMS sends the query?  
Ans:  
✅ The database **processes** the query,  
**retrieves** the required data, and sends it **back** to SSMS.
'''



'''
Q5. In the SQL flow diagram, what happens last?  
Ans:  
✅ SSMS **displays the result** on your screen after receiving it from the database.
'''



'''
Q6. Explain the SQL query journey in your own words.  
Ans:  
1️⃣ You write SQL in SSMS.  
2️⃣ SSMS sends it to the database.  
3️⃣ Database finds and returns data.  
4️⃣ SSMS shows the results to you.  

💡 Think of SSMS as a **messenger** between you and the database.
'''
# Code-style illustration:
flow = ["Write SQL →", "SSMS sends →", "Database processes →", "SSMS displays"]
print(" → ".join(flow))




'''
Q7. What role does SQL play in the process?  
Ans:  
✅ SQL is the **language** used to talk to the database —  
it tells the database *what* data to fetch or change.
'''



'''
Q8. True or False:  
SSMS directly stores data without contacting the database.  
Ans:  
❌ False.  
SSMS only sends SQL queries — the **database** actually stores and retrieves the data.
'''



'''
💡 SQL Query Flow (Simple Steps)

1️⃣ Write SQL → in SSMS  
2️⃣ SSMS → sends to database  
3️⃣ Database → finds results  
4️⃣ SSMS → shows results  

🧩 Shortcut Memory Line:
"Write → Send → Retrieve → Display"
'''
