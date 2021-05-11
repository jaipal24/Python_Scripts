# Given two integers n and k. Find position the n\’th multiple of K in the Fibonacci series.
# Examples:
# Input : k = 2, n = 3
# Output : 9
# 3rd multiple of 2 in Fibonacci Series is 34
# which appears at position 9.

if __name__ == "__main__":
    k = int(input("Enter K value:"))
    n = int(input("Enter N value:"))
    res = [0, 1]
    i = 2
    flag = True
    count = 0
    while flag:
        res.append(res[i-1]+res[i-2])
        if res[i] % k == 0:
            count = count + 1
        if count == n:
            print(i)
            flag = False
        i = i+1
