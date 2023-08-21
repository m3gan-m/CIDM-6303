#megan moore
#I'm Having issues with trying to write the values into the database. I could use some help here.

import sqlite3
import pandas as pd
import csv

with open("customers.csv") as file:
    reader=csv.reader(file)
    customers = list(reader)
    for row in customers:
        print(row)

with sqlite3.connect("chinook.db") as conn:
    command= "INSERT INTO customers(Company, FirstName, LastName, Address, City, PostalCode, Country, Email) VALUES (?,?,?,?,?,?,?,?)"
    for customer in customers:
        conn.execute(command,customer)
        conn.commit()

