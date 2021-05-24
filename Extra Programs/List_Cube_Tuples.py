# Given a list of numbers of list,
# write a Python program to create a list of tuples having first element as the number
# and second element as the cube of the number.
if __name__ == "__main__":
    lt = list(map(int, input("Enter a list of values:").split()))
    res = [(val, pow(val, 3)) for val in lt]
    print(res)
