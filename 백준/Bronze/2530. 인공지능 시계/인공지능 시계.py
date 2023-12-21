import datetime
import sys

input = sys.stdin.readline

time1 = datetime.datetime.strptime(input().rstrip(), "%H %M %S")
time2 = time1 + datetime.timedelta(seconds=int(input()))
hour = int(time2.hour)
minute = int(time2.minute)
second = int(time2.second)

result = str(hour) + " " + str(minute) + " " + str(second)
print(result)
