'''
Q1. What is a schema in a database?
Ans:
A schema is the blueprint of the database that describes what tables exist and what columns they contain.
'''
# Example: Schema includes Students(id, name, marks)

'''

Q2. Why is a schema compared to a "building plan"?
Ans:
Because it lays out the structure before data is stored, just like a plan shows rooms before construction.
'''
# Example: Schema defines tables before data is added.

'''

Q3. What is a table in a database?
Ans:
A table is a collection of related data arranged in rows and columns.
'''
# Example: Students table, Marks table, Products table.

'''

Q4. What is a column in a table?
Ans:
A column represents one attribute of the data, and each column has a name and data type.
'''
# Example: id (INT), name (TEXT), marks (INT)

'''

Q5. What is a row in a table?
Ans:
A row is one complete record containing values for each column.
'''
# Example: (1, "Aisha", 88)

'''

Q6. How are columns and rows different?
Ans:
Columns define what type of data is stored, while rows store the actual values for those columns.
'''
# Example: Column = "marks", Row value = 95.

'''

Q7. Why do databases use tables instead of one big file?
Ans:
Tables organize data clearly, avoid repetition, and make searching, updating, and managing data easier.
'''
# Example: Students stored separately from Marks to avoid duplication.

'''

Q8. How does the schema help the DBMS maintain data consistency?
Ans:
The schema enforces rules like data types, required columns, and structure, preventing invalid or inconsistent data.
'''
# Example: id must be an integer; name cannot be stored as a number.
