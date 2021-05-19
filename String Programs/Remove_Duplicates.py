# We are given a string and we need to remove all duplicates from it?
# What will be the output if the order of character matters?
# Examples:
# Input : geeksforgeeks
# Output : efgkos
from collections import OrderedDict
if __name__ == "__main__":
    s = input("Enter a string:")
    res1 = "".join(set(s))  # removes all duplicates and order does not matter
    res2 = "".join(OrderedDict.fromkeys(s))  # removes all duplicates and order of the characters is same
    print("String after removing duplicates without maintaining order:", res1)
    print("String after removing duplicates maintaining order:", res2)
