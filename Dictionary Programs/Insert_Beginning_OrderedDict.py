# Given an ordered dict, write a programm to insert items in beginning of ordered dict.
from collections import OrderedDict
if __name__ == "__main__":
    dt = OrderedDict([('akshat', '1'), ('nikhil', '2')])
    val = OrderedDict([("manjeet", '4'), ("akash", '4')])
    res = OrderedDict(list(dt.items()) + list(val.items()))
    print(res)
