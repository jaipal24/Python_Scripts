# Given a list of numbers, write a Python program to print all positive and negative numbers in given list.
def pos_neg_num(lt1):
    pos_lt = []
    neg_lt = []
    for ele in lt1:
        if ele >= 0:
            pos_lt.append(ele)
        else:
            neg_lt.append(ele)
    return [pos_lt, neg_lt]


if __name__ == "__main__":
    lt = list(map(int, input("Enter list elements:").split(" ")))
    res = pos_neg_num(lt)
    print("Positive elements in the list are:{0}".format(res[0]))
    print("Negative elements in the list are:{0}".format(res[1]))
