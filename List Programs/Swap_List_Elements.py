# Given a list, write a Python program to swap first and last element of the list.
# Approach 1: Swapping the elements using the indexes
if __name__ == "__main__":
    lt = list(input("Enter list elements:").split(" "))
    n = len(lt)
    swap = lt[0]
    lt[0] = lt[n-1]
    lt[n-1] = swap
    print(lt)

# Approach 2: The last element of the list can be referred as list[-1].
# Therefore, we can simply swap list[0] with list[-1].
# Approach 3: Using * operand.
# def swapList(list):
#     start, *middle, end = list
#     list = [end, *middle, start]
#     return list
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))
# Output:
# [24, 35, 9, 56, 12]
