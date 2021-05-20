# We are going to use regular expressions to find any url present in a string and display them.
import re


def find_url(st):
    reg = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(reg, st)
    for u in url:
        print(u[0])


if __name__ == "__main__":
    s = input("Enter a string:")
    find_url(s)
