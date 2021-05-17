# We need to find the frequency of the words in a given string
def find_frequency(str1):
    words = str1.split(" ")
    res = {}
    for key in words:
        res.__setitem__(key, words.count(key))
    # res = {key: words.count(key) for key in words} this can also be used.
    # res = dict(Counter(words)) Counter can be imported from collections as(from collections import Counter).
    return res


if __name__ == "__main__":
    s = input("Enter the string:")
    word_count = find_frequency(s)
    print(word_count)
