#  Program to compute the sum of two matrices and then print it in Python.
def sum_mat(mat1, mat2):
    res = [[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    # result = [map(sum, zip(*t)) for t in zip(mat1, mat2)] this is another way to add matrix elements.
    return res


if __name__ == "__main__":
    row = int(input("Enter number of rows:"))
    col = int(input("Enter number of columns:"))
    print("Enter matrix1 elements one by one:")
    matrix1 = [[int(input()) for j in range(col)] for i in range(row)]
    print("Enter matrix2 elements one by one:")
    matrix2 = [[int(input()) for j in range(col)] for i in range(row)]
    print("The addition of two matrices is:")
    for r in sum_mat(matrix1, matrix2):
        print(r)
