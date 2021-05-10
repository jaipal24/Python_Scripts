# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
# For example factorial of 6 is 6*5*4*3*2*1 which is 720.

def fact_fun(n):
    f = 1
    while n != 0:
        f = f * n
        n = n-1
    return f


if __name__ == "__main__":
    num = int(input("Enter number:"))
    res = fact_fun(num)
    print(res)
