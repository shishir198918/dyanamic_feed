import db
from datetime import datetime,timezone


def UTF_time_converter(DatetimeStamp):  # not in use 
    return DatetimeStamp.astimezone(timezone.utc)

def comparing_dates(published_timestamp,latest_time):
    #print(datetime_format_converter(published_timestamp),(db.latest_time(None)[0][0]))
    return datetime_format_converter(published_timestamp)>latest_time

def ISO_string(string):  
    # use for conversion "Fri, 28 Feb 2025 01:54:26 +0000" to "datetime(2025, 2, 28, 1, 54, 26, tzinfo=timezone.utc)"
    return str(datetime.strptime(string,'%a, %d %b %Y %H:%M:%S %z'))

def datetime_format_converter(timestamp):
    try:
        return (datetime.fromisoformat(timestamp))
    except:
        return datetime.fromisoformat(ISO_string(timestamp))

#print(comparing_dates("Fri, 28 Feb 2025 01:54:26 +0000"))
#print((datetime_format_converter("Fri, 28 Feb 2025 01:54:26 +0000")))

      
