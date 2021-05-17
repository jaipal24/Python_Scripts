# Write a python program to return Kth column from a matrix
def mat_k_col(mat1, k):
    res = [r[k] for r in mat1]
    return res


if __name__ == "__main__":
    row = int(input("Enter number of rows:"))
    print("Enter the matrix elements:")
    mat = [list(map(int, input().split(" "))) for i in range(row)]
    val = int(input("Enter the column to return:"))
    print("The {0} column values are:{1}".format(val, mat_k_col(mat, val-1)))
