# We are given a string and we need to reverse words of a given string
def reverse_str(str1):
    val = str1.split()
    res = ''
    for i in range(len(val)-1, -1, -1):
        res += " " + val[i]
    return res


if __name__ == "__main__":
    s = input("Enter a string:")
    print("The reverse of the given string is:\n", reverse_str(s))
    print("Reversed using built in function:\n", ' '.join(reversed(s.split(" "))))
