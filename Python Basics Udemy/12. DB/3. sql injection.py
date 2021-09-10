import sqlite3
#DON'T PUT STRINGS TO DB BUT SPARAMETER SUBSTITITION ?
db=sqlite3.connect("contacts.sqlite")

new_email="anohreremai"
phone="other value"

#update_sql="update contacts set email='{}'".format(new_email)
update_sql="update contacts set email=? where phone=?"

print(update_sql)

update_cursor=db.cursor()
#update_cursor.executescript(update_sql)
update_cursor.execute(update_sql,(new_email,phone))
print("{} rows updated".format(update_cursor.rowcount))

print()
print("are connections the same:{}".format(update_cursor.connection==db))
print()

update_cursor.connection.commit()
update_cursor.close()
for name,phone,email in db.execute("select * from contacts"):
    print(name)
    print(phone)
    print(email)
    print("-"*20)

db.close()