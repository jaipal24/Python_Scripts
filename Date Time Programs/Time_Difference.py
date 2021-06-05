# Given two times h1:m1 and h2:m2 denoting hours and minutes in 24 hours clock format.
# The current clock time is given by h1:m1.
# The task is to calculate the difference between two times in minutes and
# print the difference between two times in h:m format.
from datetime import datetime


def diff_time(h1, m1, h2, m2):
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    if t1 == t2:
        return "Both are same times"
    else:
        diff = t2 - t1
    h = int((diff / 60)) % 24
    m = diff % 60
    return str(h) + ":" + str(m)


if __name__ == "__main__":
    hrs2, min2 = map(int, input("Enter hours and minutes of checking time:").split(":"))
    hrs1, min1 = map(int, input("Enter hours and minutes of current time:").split(":"))
    res = diff_time(hrs1, min1, hrs2, min2)
    print(res)
