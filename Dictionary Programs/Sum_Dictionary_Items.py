# Given a dictionary in Python, write a Python program to find the sum of all Items in the dictionary.
def sum_dict(dt):
    res = sum([ele for ele in dt.values()])
    return res


if __name__ == "__main__":
    dict1 = {
        'a': 200,
        'b': 400,
        'c': 150,
        'd': 460
    }
    print("The sum of dictionary items is:", sum_dict(dict1))
