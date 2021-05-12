# Given a list in Python and provided the positions of the elements
# write a program to swap the two elements in the list.
def swap_elements(lt1, p1, p2):
    lt[p1], lt[p2] = lt[p2], lt[p1]
    return lt1


if __name__ == "__main__":
    lt = list(input("Enter List elements:").split(" "))
    pos1, pos2 = map(int, input("Enter the two positions to swap:").split(" "))
    print(swap_elements(lt, pos1-1, pos2-1))
