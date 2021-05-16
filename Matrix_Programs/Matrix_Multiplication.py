# Given two matrix the task is that we will have to create a program to multiply two matrices in python.
def mat_mul(mat1, mat2):
    res = [[sum(a * b for a, b in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]
    return res


if __name__ == "__main__":
    row = int(input("Enter number of rows:"))
    col = int(input("Enter number of columns:"))
    print("Enter matrix1 elements one by one:")
    matrix1 = [[int(input()) for j in range(col)] for i in range(row)]
    print("Enter matrix2 elements one by one:")
    matrix2 = [[int(input()) for j in range(col)] for i in range(row)]
    print("The multiplication of two matrices is:")
    for r in mat_mul(matrix1, matrix2):
        print(r)
