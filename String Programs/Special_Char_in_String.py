# Given a string, the task is to check if that string contains any special character
# (defined special character set).
# If any special character found, don’t accept that string.
import re


def check_spl_char(str1):
    reg = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if reg.search(str1) is None:
        return "String is Accepted"
    else:
        return "String is not Accepted"


if __name__ == "__main__":
    s = input("Enter a string")
    res = check_spl_char(s)
    print(res)
