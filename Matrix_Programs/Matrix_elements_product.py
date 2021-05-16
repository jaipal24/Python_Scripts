# Getting the product of list is quite common problem and has been dealt with and discussed many times,
# but sometimes, we require to better it and total product,
# i.e. including those of nested list as well.
def prod(val):
    res = 1
    for i in val:
        res *= i
    return res


if __name__ == "__main__":
    row = int(input("Enter number of rows:"))
    mat = [(list(map(int, input().split(" ")))) for i in range(row)]
    print("Result:", prod(ele for sub in mat for ele in sub))
