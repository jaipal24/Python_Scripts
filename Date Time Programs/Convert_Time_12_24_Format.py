# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note : Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock.
# Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock.
# Examples :
# Input : 11:21:30 PM
# Output : 23:21:30
# Input : 12:12:20 AM
# Output : 00:12:20
def convert(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:-2]


if __name__ == "__main__":
    tm = input("Enter time in (HH:MM:SS AM/PM) format i.e 12hrs format:")
    res = convert(tm)
    print("Time after converting to 24hrs format:", res)
