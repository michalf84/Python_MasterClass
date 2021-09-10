import sqlite3
db=sqlite3.connect("contacts.sqlite")
update_sql="update contacts set email='nowy adres'"
update_cursor=db.cursor()
update_cursor.execute(update_sql)
update_cursor.connection.commit()
update_cursor.close()
for row in db.execute("select * from contacts"):
    print(row)

db.close()