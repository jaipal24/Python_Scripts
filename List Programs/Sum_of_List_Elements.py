# Given a list of numbers, write a Python program to find the sum of all the elements in the list.
def sum_elements(lt1):
    sum1 = 0
    for ele in lt1:
        sum1 += ele
    return sum1
# We can also use sum(list) function to get the sum of list elements


if __name__ == "__main__":
    lt = list(map(int, input("Enter list elements:").split(" ")))
    print("Sum of the list elements: {0}".format(sum_elements(lt)))
