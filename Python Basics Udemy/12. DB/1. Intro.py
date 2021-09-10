import sqlite3
db=sqlite3.connect("contacts.sqlite")
#db.execute("drop table contacts")
db.execute("create table if not exists contacts(name text, phone integer, email text)")
#db.execute("truncate table contacts")
db.execute("insert  into contacts(name,phone,email) values ('Tim',534534,'tim@gmail.com')")
db.execute("INSERT INTO contacts (name, phone,email) values('Brian',1234,'brian@gmail.com')")

cursor=db.cursor()
cursor.execute("select * from contacts")
# for row in cursor:
#     print(row)
#
# print()

# print(cursor.fetchall())
for name,phone,email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-"*20)
cursor.close()
db.commit()
db.close()