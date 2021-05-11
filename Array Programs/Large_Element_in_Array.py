# Given an array, find the largest element in it.
# Input : arr[] = {10, 20, 4}
# Output : 20

if __name__ == "__main__":
    arr = map(int, input("Enter the array elements").split(" "))
    max1 = -9999
    for i in arr:
        if i >= max1:
            max1 = i
    print(max1)
