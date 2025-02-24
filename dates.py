import db
from datetime import datetime,timedelta,timezone


def UTF_time_converter(DatetimeStamp):
    return DatetimeStamp.astimezone(timezone.utc)

def diffrence_time(t1,t2):
    return t1-t2


times=db.latest_time(None)
print(times[0][0])
print(UTF_time_converter(times[0][0]))

#print(datetime.now(timezone.utc))
      
