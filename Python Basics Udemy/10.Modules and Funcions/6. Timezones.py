import time
import datetime
print("THe epoch on this system starts at " +time.strftime("%c",time.gmtime()))
print("The current timezeon e is {0} with an offset of {1}".format(time.tzname[0],time.timezone))

if time.daylight !=0:
    print("\t Daylight saving time is in effect for this location")
    print("\tThe DST timezone is"+time.tzname[1] )

print("Local time is :"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print("UCT time is :"+time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
print()

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

# watch this https://www.youtube.com/watch?v=-5wpm-gesOY