'''
Q1. How do relational databases maintain strong consistency?
Ans:
They use ACID transactions, which ensure all operations happen completely and consistently, even with failures.
'''
# Example: Money transfer → debit + credit must both succeed or both fail.

'''

Q2. Why do key-value databases often choose availability and partition tolerance over strong consistency?
Ans:
Because they are designed for distributed systems where fast responses and uptime matter more than strict ordering of writes.
'''
# Example: Redis, DynamoDB prioritize speed even if some nodes see updates later.

'''

Q3. In the CAP theorem, what trade-off do relational databases usually make?
Ans:
They prefer Consistency + Partition Intolerance over high availability in distributed setups.
'''
# Example: SQL databases may block writes during network splits to avoid inconsistent data.

'''

Q4. How do key-value stores scale compared to relational databases?
Ans:
Key-value stores scale horizontally very easily by distributing keys across many machines.
'''
# Example: AWS DynamoDB automatically spreads keys across servers.

'''

Q5. Why is sharding difficult in relational databases?
Ans:
Because JOINs across shards and maintaining foreign-key relationships become complex and slow.
'''
# Example: Joining Students and Marks across different servers is expensive.

'''

Q6. When is a key-value database a better choice than a relational database?
Ans:
When the workload needs extremely fast reads/writes, simple access patterns, or large-scale distributed storage.
'''
# Example: Caching, leaderboards, session storage, real-time counters.

'''

Q7. When is a relational database the better choice?
Ans:
When the data has relationships, requires constraints, and needs complex queries or strict consistency.
'''
# Example: Banking, inventory, school management systems with linked tables.
