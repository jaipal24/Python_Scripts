# A string is given, and you have to find all the words
# (substrings separated by a space)
# which are greater than the given length k.
def greater_k(str1, k):
    res = []
    for ele in str1.split(" "):
        if len(ele) > k:
            res.append(ele)
    return res


if __name__ == "__main__":
    string = input("Enter a string of words:")
    size = int(input("Enter the word size:"))
    print("The words with length greater than {0} is {1}".format(size, greater_k(string, size)))
