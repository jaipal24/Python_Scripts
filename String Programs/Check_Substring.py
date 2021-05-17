# We need to write a program to check is a string is present in other string
import re


def check_substring1(str1, str2):
    if str1.find(str2) == -1:
        print("No")
    else:
        print("Yes")


def check_substring2(str1, str2):
    if str1.count(str2) > 0:
        print("Yes")
    else:
        print("No")


def check_substring3(str1, str2):
    if re.search(str2, str1):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    s1 = input("Enter the string1:")
    s2 = input("Enter the string2:")
    print("Checking the substring in the string using find():")
    check_substring1(s1, s2)
    print("Checking the substring in the string using count():")
    check_substring2(s1, s2)
    print("Checking the substring in the string using regular expression re.search():")
    check_substring3(s1, s2)
