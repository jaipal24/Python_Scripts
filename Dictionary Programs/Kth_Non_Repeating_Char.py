# Given a string and a number k, find the k-th non-repeating character in the string.
from collections import OrderedDict


def k_non_rep_char(st, k):
    dt = OrderedDict.fromkeys(st, 0)
    for ch in st:
        dt[ch] += 1
    lt = [key for key, value in dt.items() if value == 1]
    if len(lt) < k:
        return "Less than k non-repeating characters in input."
    else:
        return lt[k-1]


if __name__ == "__main__":
    s = input("Enter a string:")
    val = int(input("Enter k value:"))
    res = k_non_rep_char(s, val)
    print(res)
