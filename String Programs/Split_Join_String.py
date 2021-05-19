# Python program to Split a string based on a delimiter and join the string using another delimiter.
if __name__ == "__main__":
    s = input("Enter a string with space delimiter:")
    lt = s.split(" ")
    res = "-".join(lt)
    print(res)
