# Given a number x, determine whether the given number is Armstrong number or not.
# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

def armstrong_number(n, l):
    temp = n
    res=0
    while temp > 0:
        res = res + pow(temp % 10, l)
        temp = temp // 10
    if res == num:
        return "Given number is Armstrong Number"
    else:
        return "Given number is not an Armstrong Number"


if __name__ == "__main__":
    str1 = input("Enter Number:")
    N = len(str1)
    num = int(str1)
    val = armstrong_number(num, N)
    print(val)
