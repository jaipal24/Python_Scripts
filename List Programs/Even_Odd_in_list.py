# Given a list of numbers, write a Python program to print all even numbers in given list.
def odd_list(lt1):
    res1 = []
    for ele in lt1:
        if ele % 2 != 0:
            res1.append(ele)
    return res1


def even_list(lt2):
    res2 = []
    for ele in lt2:
        if ele % 2 == 0:
            res2.append(ele)
    return res2


if __name__ == "__main__":
    lt = list(map(int, input("Enter elements into list:").split(" ")))
    print("Odd elements in the list:", odd_list(lt))
    print("Even elements in the list:", even_list(lt))
