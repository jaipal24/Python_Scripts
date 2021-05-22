# Given two numbers you are required to check whether
# they are anagrams of each other or not in binary representation.
from collections import Counter


def check_anagram(n1, n2):
    bn1, bn2 = bin(n1)[2:], bin(n2)[2:]
    zeros = abs(len(bn1)-len(bn2))
    if len(bn1) > len(bn2):
        bn2 = zeros * '0' + bn2
    else:
        bn1 = zeros * '0' + bn1
    dt1 = Counter(bn1)
    dt2 = Counter(bn2)
    if dt1 == dt2:
        return True
    else:
        return False


if __name__ == '__main__':
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    res = check_anagram(num1, num2)
    if res:
        print("Given two numbers are anagrams in their binary representation!!")
    else:
        print("Given two numbers binary representations are not an anagram!!")
