# Given two positive integers start and end.
# The task is to write a Python program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# The first few prime numbers are {2, 3, 5, 7, 11, ….}.
# The idea to solve this problem is to iterate the val from start to end using a for loop and for every number,
# if it is greater than 1, check if it divides n.
# If we find any other number which divides, print that value.

def check_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count = count+1
    if count == 2:
        return True
    else:
        return False


if __name__ == "__main__":
    start = int(input("Enter starting value:"))
    end = int(input("Enter ending value:"))
    for i in range(start, end+1):
        if check_prime(i):
            print(i)
