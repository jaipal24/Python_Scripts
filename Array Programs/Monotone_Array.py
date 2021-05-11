# Given an array A containing n integers.
# The task is to check whether the array is Monotonic or not.
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].
# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
# Return “True” if the given array A is monotonic else return “False” (without quotes).
# Examples:
# Input : 6 5 4 4
# Output : true
# Input : 5 15 20 10
# Output : false

from array import *

if __name__ == "__main__":
    arr = array('i', map(int, input("Enter array elements:").split(" ")))
    inc_count = 0
    dec_count = 0
    for i in range(len(arr)-1):
        if arr[i] <= arr[i+1]:
            inc_count = inc_count+1
        elif arr[i] >= arr[i+1]:
            dec_count = dec_count+1
    if inc_count == len(arr)-1 or dec_count == len(arr)-1:
        print("True")
    else:
        print("False")
