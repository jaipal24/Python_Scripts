# We have problem in which we need to perform a case conversion of String.
# Input : left_index
# Output : leftIndex
if __name__ == "__main__":
    s = input("Enter a string in snake_case:")
    res = s.replace("_", " ").title().replace(" ", "")
    # res = string.capwords(s.replace("_", " ")).replace(" ", "") /import string/ we can also use this method
    print("The PascalCase string is:", res)
