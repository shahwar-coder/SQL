'''
Q1. What is the core data model of a relational database?
Ans:
Relational databases use the table model with rows, columns, and defined relationships using keys.
'''
# Example: Students(id, name) linked to Marks(student_id, score).

'''

Q2. What is the core data model of a key-value store?
Ans:
It stores data as key → value pairs, where the value can be any object (string, JSON, etc.).
'''
# Example: "user:1" → {"name":"Aisha", "marks":88}

'''

Q3. Why are relational databases good for structured data?
Ans:
Because they enforce schemas, constraints, and relationships, ensuring data is consistent.
'''
# Example: You can't insert two rows with the same primary key.

'''

Q4. Why are key-value stores extremely fast?
Ans:
Because they access data directly using the key without scanning tables or performing joins.
'''
# Example: Redis fetches a key in O(1) time.

'''

Q5. When should you *not* use a key-value database?
Ans:
When your data needs relationships, constraints, or complex queries like JOINs.
'''
# Example: Linking students to marks requires relational structure.

'''

Q6. What type of queries do relational databases support that key-value stores cannot?
Ans:
SQL-based queries including filtering, sorting, aggregations, and joins.
'''
# Example: SELECT AVG(marks) FROM Marks;

'''

Q7. Why are key-value stores preferred for caching or session management?
Ans:
Because they provide simple, fast read/write operations with minimal overhead.
'''
# Example: Storing "session:userid123" → "logged_in"
