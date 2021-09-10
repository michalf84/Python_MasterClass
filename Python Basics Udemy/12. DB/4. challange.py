import sqlite3
conn=sqlite3.connect("contacts.sqlite")

name=input("please enter name to seach for")
for row in conn.execute("select * from contacts where name=?",(name,)):
    print(row)

conn.close()