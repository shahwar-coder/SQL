'''
Q1. What is the main difference between SQL and NoSQL databases?
Ans:
SQL databases store data in tables, while NoSQL databases store data in flexible formats like documents, key-value pairs, columns, or graphs.
'''
# Example: MySQL uses tables; MongoDB uses documents.

'''

Q2. Why are SQL databases called "relational"?
Ans:
Because their tables can be linked using keys like primary keys and foreign keys.
'''
# Example: Students table linked to Marks table.

'''

Q3. What type of NoSQL database stores data as JSON-like documents?
Ans:
Document databases.
'''
# Example: MongoDB stores {"name":"Ali", "age":20}

'''

Q4. Which NoSQL type is the fastest for simple lookups?
Ans:
Key-value databases, because they retrieve data directly using the key.
'''
# Example: Redis → "user:1" → value

'''

Q5. When are column-based NoSQL databases useful?
Ans:
They are useful for analytical workloads and very large datasets because they read specific columns efficiently.
'''
# Example: Cassandra used for large-scale analytics.

'''

Q6. What problem type fits graph databases best?
Ans:
Problems that involve relationships, such as networks, recommendations, and connections between people or objects.
'''
# Example: Neo4j for "friend of a friend" queries.

'''

Q7. When should you choose SQL over NoSQL?
Ans:
Choose SQL when the data is structured, requires relationships, and needs strong consistency or complex queries.
'''
# Example: Banking, inventory, school management systems.


'''
Q8. What are the main types of SQL and NoSQL databases?
Ans:
SQL databases mainly follow the relational table model.  
NoSQL databases have four types: Document, Key-Value, Column-based, and Graph databases.
'''
# Example:
# SQL → MySQL, PostgreSQL  
# Document → MongoDB  
# Key-Value → Redis  
# Column → Cassandra  
# Graph → Neo4j
