# Given an unsorted list of some elements(may or may not be integers),
# Find the frequency of each distinct element in the list using a dictionary.
def frequency(lt):
    freq = {}
    for ele in lt:
        if ele in freq:
            freq[ele] += 1
        else:
            freq[ele] = 1
    return freq


if __name__ == "__main__":
    l = list(input("Enter list elements:").split())
    res = frequency(l)
    for key, val in res.items():
        print(key, ":", val)
