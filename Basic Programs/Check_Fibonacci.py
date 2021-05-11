# Given a number n, how to check if n is a Fibonacci number.
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 141, ..

if __name__ == "__main__":
    num = int(input("Enter a number:"))
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    flag = False
    while f3 <= num:
        f3 = f1 + f2
        if f3 == num:
            flag = True
        f1 = f2
        f2 = f3
    if flag:
        print("Yes")
    else:
        print("No")
