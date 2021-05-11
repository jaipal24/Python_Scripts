# Given an array of integers, find the sum of its elements.
# Examples :
# Input : arr[] = {1, 2, 3}
# Output : 6
# 1 + 2 + 3 = 6

if __name__ == "__main__":
    arr = map(int, input("Enter array elements").split(" "))
    sum1 = 0
    for i in arr:
        sum1 = sum1+i
    print(sum1)
