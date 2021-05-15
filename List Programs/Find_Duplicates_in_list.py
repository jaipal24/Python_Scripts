# Given a list of integers with duplicate elements in it.
# The task to generate another list, which contains only the duplicate elements.
# In simple words, the new list should contain the elements which appear more than one.
# Examples :
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]
def duplicates(lt1):
    dup = []
    for e1 in lt1:
        count = 0
        for e2 in lt1:
            if e1 == e2:
                count += 1
        if count > 1 and e1 not in dup:
            dup.append(e1)
    return dup


if __name__ == "__main__":
    lt = list(map(int,input("Enter list elements:").split(" ")))
    res = duplicates(lt)
    if len(res) > 0:
        print("The duplicate elements in the list are:", res)
    else:
        print("There are no duplicate elements in the list")
