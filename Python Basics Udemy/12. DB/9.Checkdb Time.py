import sqlite3
import pytz

#METHOD 1
db=sqlite3.connect("accounts.sqlite")
for row in db.execute("select * from history"):
    #print(row) this returned time as string
    local_time=row[0]
    print("{}\t{}".format(local_time,type(local_time)))

db.close()


#METHOD 2
db2=sqlite3.connect("accounts.sqlite",detect_types=sqlite3.PARSE_DECLTYPES)
for row in db2.execute("select * from history"):
    #print(row) this returned time as string
    local_time=row[0]
    print("{}\t{}".format(local_time,type(local_time)))

db.close()
print()

#METHOD 2 more chang3s to recognize timezone note you won't see it here as i would need to write data to DB in the right format
db3=sqlite3.connect("accounts.sqlite",detect_types=sqlite3.PARSE_DECLTYPES)
for row in db3.execute("select * from history"):
    utc_time=row[0]
    local_time=pytz.utc.localize(utc_time).astimezone()
    print("{}\t{}".format(utc_time,type(local_time)))
db.close()

print("METHOD 3")
#METHOD 3
db3=sqlite3.connect("accounts.sqlite",detect_types=sqlite3.PARSE_DECLTYPES)
for row in db3.execute("select strftime('%Y-%m-%d %H:%M:%f',history.time,'localtime' ) as localtime,"
                       "history.account,history.amount from history order by history.time"):
    print(row)
db.close()