#Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called Applicants using webflask
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this script:
# python New_table.py

import sqlite3

conn = sqlite3.connect('database.db')
print("Connected sucessfully to database")

conn.execute('CREATE TABLE Applicants (name TEXT, email TEXT, phone_number TEXT, job_title TEXT)')


print("Created Applicants Table successfully!")

conn.close()
