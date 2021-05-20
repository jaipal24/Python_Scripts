# Given a string of size n, write functions to perform following operations on string.
# Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
# Right (Or clockwise) rotate the given string by d elements (where d <= n).
def left_right_rotate(st, d):
    left_rotate = st[d:] + st[0:d]
    right_rotate = st[len(st)-d:] + st[0:len(st)-d]
    print("String after {0} left rotations:".format(d), left_rotate)
    print("String after {0} right rotations:".format(d), right_rotate)


if __name__ == "__main__":
    s = input("Enter a string:")
    val = int(input("Enter number of rotations:"))
    left_right_rotate(s, val)
