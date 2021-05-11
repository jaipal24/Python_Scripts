# Print the sum of series 1^3 + 2^3 + 3^3 + 4^3 + …….+ n^3 till n-th term.

if __name__ == "__main__":
    N = int(input("Enter a positive number:"))
    sum = 0
    for i in range(1, N+1):
        sum = sum + pow(i, 3)
    print(sum)
