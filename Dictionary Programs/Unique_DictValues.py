# We are given a dictionary with a list of values for each key.
# We need to get all the unique values from that dictionary.
def get_unique(dt):
    res = list(sorted({ele for val in dt.values() for ele in val}))
    return res


if __name__ == "__main__":
    dict1 = {
        "a": [2, 5, 9, 4],
        "b": [5, 8, 7, 1],
        "c": [10, 3, 9, 5]
    }
    print("The unique values in the dictionary are:", get_unique(dict1))
