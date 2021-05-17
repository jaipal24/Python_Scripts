# Given a string. the task is to check if the string is symmetrical and palindrome or not.
# A string is said to be symmetrical if both the halves of the string are the same and
# a string is said to be a palindrome string if one half of the string is the reverse of the other half or
# if a string appears same when read forward or backward.
# Example:
# Input1: khokho
# Output1:
# The entered string is symmetrical
# The entered string is not palindrome
# Input2:amaama
# Output2:
# The entered string is symmetrical
# The entered string is palindrome
def check_similar(str1):
    if len(str1) % 2 == 0:
        s1 = str1[:int(len(str1) / 2)]
        s2 = str1[int(len(str1) / 2):]
        if s1 == s2:
            print("The entered string is symmetrical")
        else:
            print("The entered string is not symmetrical")
    else:
        print("The entered string is not symmetrical")


def check_palindrome(str2):
    temp = str2.split()
    j = len(temp)-1
    for i in range(len(temp)):
        if temp[i] == temp[j]:
            j -= 1
            continue
        else:
            return "The entered string is not palindrome"
    return "The entered string is palindrome"


if __name__ == "__main__":
    s = input("Enter the string:")
    check_similar(s)
    print(check_palindrome(s))
