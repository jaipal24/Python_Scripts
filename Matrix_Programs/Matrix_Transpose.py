# Write a python program to transpose a matrix:
def mat_tran(mat1):
    res = [[mat1[j][i] for j in range(len(mat1))] for i in range(len(mat1[0]))]
    return res


if __name__ == "__main__":
    row = int(input("Enter number of rows in the matrix:"))
    mat = [list(map(int, input().split(" "))) for i in range(row)]
    print("Transpose of the given matrix is:")
    for r in mat_tran(mat):
        print(r)
