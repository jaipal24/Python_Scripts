# Traversing the list elements and multiplying them.
import numpy


def mul_elements(lt1):
    mul = 1
    for ele in lt1:
        mul *= ele
    return mul


def use_prod(lt2):
    return numpy.prod(lt2)  # Using numpy.prod() function to multiply list elements


if __name__ == "__main__":
    List1 = list(map(int, input("Enter list1 elements:").split(" ")))
    List2 = list(map(int, input("Enter list2 elements:").split(" ")))
    print("Multiplication of the list elements using traversing: {0}".format(mul_elements(List1)))
    print("Multiplication of the list elements using numpy.prod(): {0}".format(mul_elements(List2)))
