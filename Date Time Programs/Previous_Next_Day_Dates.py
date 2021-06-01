# This python programs prints the previous and the next days dates
from datetime import  datetime, timedelta

if __name__ == '__main__':
    present_day = datetime.now()
    yesterday = present_day - timedelta(1)
    tomorrow = present_day + timedelta(1)
    print("Yesterday:{0}\nToday:{1}\nTomorrow:{2}".format(yesterday.strftime("%d-%m-%Y"), present_day.strftime("%d-%m-%Y"), tomorrow.strftime("%d-%m-%Y")))
