# Given a positive integer N. The task is to find 1^2 + 2^2 + 3^2 + ….. + N^2.

if __name__ == "__main__":
    N = int(input("Enter a positive number:"))
    sum = 0
    for i in range(1, N+1):
        sum = sum+pow(i, 2)
    print(sum)
