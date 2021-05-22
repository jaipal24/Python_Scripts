# We are having a dictionary with keys and lists as their values.
# We need to sort the dictionary based on keys and also sort the list values.
def sort_key_value_list(dt):
    temp = dict()
    for key in sorted(dt):
        temp[key] = sorted(dt[key])
    return temp


if __name__ == "__main__":
    d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
    print("Dictionary:", d)
    res = sort_key_value_list(d)
    print("Dictionary after sorting:", res)
