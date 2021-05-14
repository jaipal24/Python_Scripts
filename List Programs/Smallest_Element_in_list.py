# Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
# Examples:
# Input : list1 = [10, 20, 4]
# Output : 4
# Here we will find the smalled element in the list using different possible approaches.
def min_general(lt1):
    min_val = 999999
    for ele in lt1:
        if ele < min_val:
            min_val = ele
    return min_val


def min_list_indexing(lt2):
    lt2.sort()
    return lt2.__getitem__(0)


if __name__ == "__main__":
    lt = list(map(int, input("Enter list elements:").split(" ")))
    print("Comparing element by element to find min value:{0}".format(min_general(lt)))
    print("Sorting the list and displaying first element in list:{0}".format(min_list_indexing(lt)))
    print("Using built in method min():{0}".format(min(lt)))
