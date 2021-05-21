# The aim of this program is to delete a key from a dictionary
if __name__ == "__main__":
    dict1 = {
        'a': 20,
        'b': 30,
        'c': 25,
        'd': 50,
        'e': 35
    }
    print("Dictionary in the beginning:", dict1)
    del dict1['b']
    print("Deleting b from dictionary using del keyword and dictionary after deletion:", dict1)
    dict1.pop('e')
    print("Deleting e from dictionary using pop function and dictionary after deletion:", dict1)
    # we can remove the key in a conventional way
    new_dict = {key: value for key, value in dict1.items() if 'c' != key}
    print("Deleted c in a conventional way:", new_dict)
