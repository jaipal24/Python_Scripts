# Given a pair of non empty strings.
# Count the number of matching characters in those strings
# (consider the single count for the character which have duplicates in the strings).
def count_chars(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    res = set1 & set2
    print("The count of matching characters:", len(res))


if __name__ == "__main__":
    s1 = input("Enter string1:")
    s2 = input("Enter string2:")
    count_chars(s1, s2)
