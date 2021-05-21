# Given an input string and a pattern, check if characters in the input string
# follows the same order as determined by characters present in the pattern.
# Assume there won’t be any duplicate characters in the pattern.
from collections import OrderedDict


def check_order(st, ch):
    ind = 0
    od = OrderedDict.fromkeys(st)
    for k, v in od.items():
        if k == ch[ind]:
            ind += 1
        if ind == len(ch):
            return True
    return False


if __name__ == "__main__":
    s = input("Enter a string:")
    c = input("Enter a character sequence:")
    if check_order(s, c):
        print("The characters are in an order as the sequence!!")
    else:
        print("The characters are not in an order as the sequence!!")
