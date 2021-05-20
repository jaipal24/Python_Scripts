# A permutation, also called an “arrangement number” or “order”,
# is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself.
# A string of length n has n! permutation.
from itertools import permutations


def str_permutations(str1):
    res = permutations(str1)
    for ele in list(res):
        print("".join(ele))


if __name__ == "__main__":
    s = input("Enter a string:")
    str_permutations(s)
