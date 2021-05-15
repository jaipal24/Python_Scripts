# Sometimes, while working with python data,
# we can have a problem in which we need to filter out certain empty data.
# These can be None, empty string etc. This can have application in many domains.
if __name__ == "__main__":
    lt = [3, [], 5, [], 6, 7]
    res1 = list(filter(None, lt))  # applying filter function to remove empty list
    res2 = [ele for ele in lt if ele != []]  # iterating and removing the empty list elements
    print("Using filter function:", res1)
    print("Using general approach:", res2)
