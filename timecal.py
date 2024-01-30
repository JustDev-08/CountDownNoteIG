from datetime import datetime, timedelta
import pytz
dt1 = datetime.now()
dt2 = datetime(year=2024, month=1, day=1, hour=0)
difference = dt2-dt1
sec = difference.total_seconds()
print(int(sec//3600), "Hour", int((sec/3600-sec//3600)*60), "Minute")