# Given a dictionary, perform append of keys followed by values in list.
# Input : test_dict = {“Gfg” : 1, “is” : 2, “Best” : 3}
# Output : [‘Gfg’, ‘is’, ‘Best’, 1, 2, 3]
from itertools import chain
if __name__ == "__main__":
    dt = {"I": 1, "am": 2, "the": 3, "best": 4}
    # res = list(dt.keys()) + list(dt.values()) we can also use + operator to add the lists
    res = list(chain(dt.keys(), dt.values()))
    print(res)
