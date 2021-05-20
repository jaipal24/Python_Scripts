# Given a string, find all the duplicate characters which are similar to each others.
from collections import Counter


def dup_char(st):
    wc = Counter(st.lower())
    j = -1
    for i in wc.values():
        j = j + 1
        if i > 1:
            print(list(wc.keys())[j])


if __name__ == "__main__":
    s = input("Enter a string:")
    dup_char(s)
