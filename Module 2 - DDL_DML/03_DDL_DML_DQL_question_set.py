'''SET-1
Q1) What is DDL?
A1) DDL is a set of commands used to create or change tables in a database. 
    Think of it as building or renovating the structure.

Q2) What is DML?
A2) DML is used to add, change, or remove data inside tables. 
    Think of it as writing or erasing information on a page.

Q3) What is DQL?
A3) DQL is used to read data from the database. 
    It simply answers questions about the stored data.

Q4) How are DDL and DML different?
A4) DDL changes the table itself; DML changes the data inside the table.

Q5) Does DQL change the data?
A5) No, DQL only fetches and shows data; it never modifies anything.

Q6) Which category does SELECT belong to?
A6) SELECT belongs to DQL because it retrieves information.
'''

# ======================================

'''SET-2
Q1) What does DDL do in SQL?
A1) DDL defines or modifies the structure of the database (tables, columns).
    Example commands: CREATE, ALTER, DROP.
Example:
CREATE TABLE Students (id INT, name VARCHAR(50));

Q2) What does DML do in SQL?
A2) DML is used to insert, update, and delete rows from tables.
    Example commands: INSERT, UPDATE, DELETE.
Example:
INSERT INTO Students VALUES (1, 'Aisha');

Q3) What does DQL do?
A3) DQL is used to query or read data without changing it.
    Example: SELECT.
Example:
SELECT name FROM Students WHERE id = 1;

Q4) Why can't SELECT be part of DML?
A4) Because SELECT does not modify data; it only retrieves it.

Q5) Does DROP TABLE belong to DML or DDL?
A5) DROP TABLE is DDL because it removes the entire table structure, not just data.

Q6) Which category affects the number of rows in a table?
A6) DML affects the row count (INSERT adds rows, DELETE removes rows).

Q7) Which category affects the number of columns in a table?
A7) DDL affects columns (ALTER TABLE ADD column).
'''
