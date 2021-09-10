import time
# monotonic and perf_counter have better precision and time cannot go backwards
# process_time gives cpu time
import random
print(time.gmtime(0))
print(time.localtime())
print(time.localtime(time.time()))
print(time.time())

time_here=time.localtime()
print(time_here)
print("Year",time_here[0],time_here.tm_year)
print("Month",time_here[1],time_here.tm_mon)
print("Day",time_here[2],time_here.tm_mday)

print(time.localtime().tm_year)
print()

print("time()\t",time.get_clock_info("time"))
print("perf_counter()\t",time.get_clock_info("perf_counter"))
print("monotonic()\t",time.get_clock_info("monotonic"))
print("process_time\t",time.get_clock_info("process_time"))
