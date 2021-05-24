# Given a string and a number N,
# we need to mirror the characters from N-th position up to the length of the string in the alphabetical order.
# In mirror operation, we change ‘a’ to ‘z’, ‘b’ to ‘y’, and so on.
def mirror_char(st, pos):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rev = "zyxwvutsrqponmlkjihgfedcba"
    val = ""
    str1 = st[pos:]
    for ch in str1:
        ind = alpha.find(ch)
        if ind != -1:
            val += rev[ind]
    return st[:pos]+val


if __name__ == "__main__":
    s = input("Enter a string:")
    n = int(input("Enter a position:"))
    res = mirror_char(s, n)
    print(res)
