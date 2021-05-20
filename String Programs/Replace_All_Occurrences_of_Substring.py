# Sometimes, while working with Python strings,
# we can have a problem in which we need to replace all occurrences of a substring with other.
# We use maketrans() and translate(). This is inbuild way to perform this task.
# This function maintains the table internally and performs the task of swapping.
if __name__ == "__main__":
    string = input("Enter the main string:")
    sub_str = input("Enter substring to replace:")
    rep = input("Enter replacing word:")
    tran = string.maketrans(sub_str, rep)
    string = string.translate(tran)
    print("The string after replacing all occurrences of {0}".format(sub_str), string)
# But here we have a problem we can only replace the substring with another word of same size.
