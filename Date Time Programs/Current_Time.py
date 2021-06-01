# This program will get the current time based on the given timezone.
from datetime import *
import pytz

if __name__ == "__main__":
    tz_India = pytz.timezone("Asia/Kolkata")
    date_time_India = datetime.now(tz_India)
    print("IST:", date_time_India.strftime("%H:%M:%S"))
    print("UTC:", datetime.now(pytz.utc).time())
