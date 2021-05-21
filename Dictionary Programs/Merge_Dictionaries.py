# In this program we will be merging two dictionaries.
if __name__ == "__main__":
    d1 = {'a': 10, 'b': 8}
    d2 = {'d': 6, 'c': 4}
    # we can use update function to merge both the dictionaries.
    temp = d1
    temp.update(d2)
    print("Using update function:", temp)
    print("Using | operator:", d1 | d2)
