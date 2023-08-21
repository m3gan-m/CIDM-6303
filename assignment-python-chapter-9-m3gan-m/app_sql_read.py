import sqlite3
#MEGAN MOORE
#must have completed the SQLite writing to Movies databse prior to this task
#Read from a SQLite database
print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies"
    cursor = conn.execute(sql_command)
    for row in cursor:
        #row is a tuple
        print(f"The movie {row[1]} was released in {row[2]}")


#modify the sql command to filter data
#remember you select from where statements? Now you can use them
print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    #sql command can be any select sql statement to get the data you need
    sql_command = "SELECT * FROM Movies WHERE Year > 1985"
    cursor = conn.execute(sql_command)
    for row in cursor:
        #row is a tuple. Access the tuple's values with row [index number]
        #each row in the tuple corresponds to a row in the table
        #returned by the sql command
        print(f"The movie {row[1]} was released in {row[2]}")


#ANother way to read form a Sqlite database using cursor.fetchall()
#which returns all the data into a python list
print("Getting data")
db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    sql_command = "SELECT * FROM Movies"
    cursor = conn.execute(sql_command)
    movies = cursor.fetchall()
    print(movies)
"""
Note
You now have a variable movies, which is a list of all the data in the database
each row in the typle corresponds to a row in the table returned by the sql command
"""