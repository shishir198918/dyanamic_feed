import db
from datetime import datetime,timezone


def UTF_time_converter(DatetimeStamp):  # not in use 
    return DatetimeStamp.astimezone(timezone.utc)

def comparing_dates(published_timestamp):
    #print(datetime_format_converter(published_timestamp),(db.latest_time(None)[0][0]))
    return datetime_format_converter(published_timestamp)>(db.latest_time(None)[0][0])

def datetime_format_converter(timestamp):
    return (datetime.fromisoformat(timestamp))

#print(comparing_dates("2025-02-18T07:08:29.757659+00:00",db.latest_time(None)))
#print(db.latest_time(None)[0][0])

      
