# We are given a tuple and need to find the minimum and maximum k values in that tuple
if __name__ == "__main__":
    tp = tuple(map(int, input("Enter tuple elements").split(" ")))
    k = int(input("Enter no of elements:"))
    res = ()
    if k <= len(tp):
        sorted_lt = sorted(list(tp))
        res = tuple(sorted_lt[:k]+sorted_lt[len(tp)-k:])
    print(res)
