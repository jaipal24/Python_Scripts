# Given a list in Python and a number x, count number of occurrences of x in the given list.
# Examples:
# Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x = 10
# Output : 3

def count_occ(lt1, k):
    count = 0
    for ele in lt1:
        if k == ele:
            count += 1
    return count


if __name__ == "__main__":
    lt = list(input("Enter list elements:").split(" "))
    val = input("Enter the value to find its occurrence:")
    print("The value is found {0} time in the list:".format(count_occ(lt,val)))
