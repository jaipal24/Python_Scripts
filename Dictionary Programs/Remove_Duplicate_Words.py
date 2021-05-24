# Given a sentence containing n words/strings.
# Remove all duplicates words/strings which are similar to each others.
from collections import Counter
if __name__ == "__main__":
    words = input("Enter a sentence:").split()
    dt = dict(Counter(words))
    res = list(ele for ele in dt.keys())
    print(res)
