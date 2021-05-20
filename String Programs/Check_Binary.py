# Given a string str. The task is to check whether it is a binary string or not.
def check_bin(str1):
    st = set(str1)
    check = {'0', '1'}
    if st == check or st == {'0'} or st == {'1'}:
        return "Binary String"
    else:
        return "Not a Binary String"


if __name__ == "__main__":
    s = input("Enter a string:")
    print(check_bin(s))
