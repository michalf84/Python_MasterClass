import datetime
import pytz

local_time=datetime.datetime.now()
utc_time=datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Utc time: {}".format(utc_time))

aware_local_time=pytz.utc.localize(local_time)
aware_utc_time=pytz.utc.localize((utc_time))

print("Aware local time {}, timezone {}".format(aware_local_time,aware_local_time.tzinfo))
# the above does not have timezone thus the query will not result datatime adjustment will always be +0. so store data in utc and c
# convert when displayed, the below solution prompts timezone of local system
#----------
aware_local_time=pytz.utc.localize(local_time).astimezone()
print("Aware local time {}, timezone {}".format(aware_local_time,aware_local_time.tzinfo))
#-----------
print("Aware UTC {}, time zone {}".format(aware_utc_time,aware_utc_time.tzinfo))

print()

gap_time=datetime.datetime(2015,10,25,1,30,0,0)
print(gap_time)
print(gap_time.timestamp())

s=144573000
t=s+(60*60)
gb=pytz.timezone('GB')

dt1=pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
dt2=pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s,dt1))
print("{} seconds since the epoch is {}".format(t,dt2))
print(""*20)
# have utc in method to give correct rsult
dt1=pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2=pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s,dt1))
print("{} seconds since the epoch is {}".format(t,dt2))