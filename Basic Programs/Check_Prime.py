# Given a positive integer N, The task is to write a Python program to check if the number is prime or not.

if __name__ == "__main__":
    num = int(input("Enter a number:"))
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count+1
    if count == 2:
        print("{0} is a prime number".format(num))
    else:
        print("{0} is not a prime number".format(num))
