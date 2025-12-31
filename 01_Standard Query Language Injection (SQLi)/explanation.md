# SQL Injection (SQLi) Explained

### The Concept
Imagine you are filling out a paper form. SQL Injection is like writing "Please give me all the files" in the name field, and the clerk actually doing it because they follow instructions blindly.

### The Flaw
The vulnerable code concatenates strings:
`"SELECT * FROM users WHERE name = '" + user_input + "'"`
This mixes **Data** (your name) with **Code** (the SQL command).

### The Fix
**Parameterized Queries** separate the data from the code. The database is told: "Here is the command, and here is the data to put in the placeholder."