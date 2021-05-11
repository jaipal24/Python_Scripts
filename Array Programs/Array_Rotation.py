# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.

from array import *


def rotate(arr1, rot, n):
    for i in range(rot):
        temp = arr1[0]
        for j in range(n-1):
            arr1[j] = arr1[j+1]
        arr1[n-1] = temp


if __name__ == "__main__":
    arr = array('i',map(int,input("Enter array elements:").split(" ")))
    d = int(input("Enter no of rotations:"))
    rotate(arr, d, len(arr))
    for i in arr:
        print(i)
