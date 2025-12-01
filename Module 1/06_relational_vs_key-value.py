'''
Q1. What is a relational database?
Ans:
It is a database that stores data in tables like rows and columns.
'''
# Example: A Students table with id, name, marks.

'''

Q2. What is a key-value database?
Ans:
It stores data as pairs: a key and its value (like a dictionary).
'''
# Example: "user1" → {"name":"Aisha"}

'''

Q3. What is the biggest difference between the two?
Ans:
Relational databases use tables, but key-value databases use key→value pairs.
'''
# Example: MySQL uses tables; Redis uses key→value.

'''

Q4. Which one allows relationships between data?
Ans:
Relational databases allow relationships; key-value stores do not.
'''
# Example: Students linked to Marks using student_id.

'''

Q5. Which one is simpler and faster for quick lookups?
Ans:
Key-value databases are simpler and very fast for finding data by key.
'''
# Example: Asking for value of "user1" instantly.

'''

Q6. Which one uses SQL?
Ans:
Relational databases use SQL.
'''
# Example: SELECT * FROM Students WHERE id=1;

'''

Q7. When would you use a key-value database?
Ans:
When you just need to store and fetch data quickly using a key.
'''
# Example: Storing login sessions or cached data.


'''
===================================================================
                RELATIONAL DATABASE vs KEY–VALUE DATABASE
===================================================================

                  RELATIONAL DATABASE (SQL)                   KEY–VALUE DATABASE (NoSQL)
                  -----------------------------               ----------------------------
  Structure:      Tables with rows & columns                  Key → Value pairs (dictionary)

                    +------------------------+                  "user1" → {name:"Aisha"}
                    |   STUDENTS TABLE      |
                    +------------------------+
                    | id | name | marks     |
                    +----+------+-----------+

  Relationships:   YES — tables can link using keys            NO — values are independent
                    (student_id → marks table)                   (no relational linking)

  Querying:        Uses SQL                                     No SQL (simple GET by key)
                    SELECT * FROM Students                       GET "user1"
                    WHERE id = 1;

  Best for:        Structured data, relationships               Fast lookups, caching, sessions
                    (e.g., Students ↔ Marks)                      (fetch key instantly)

  Examples:        MySQL, PostgreSQL                            Redis, DynamoDB

===================================================================
BIG DIFFERENCE:
Relational DB = Tables + SQL + Relationships  
Key-Value DB = Key → Value + Super fast lookup + No relationships
==================================================================='''
