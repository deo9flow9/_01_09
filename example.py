import pytz
import datetime
import time

print(time.tzname[0])
print(pytz.utc.localize(datetime.datetime.utcnow()).astimezone())