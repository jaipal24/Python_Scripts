# Given a String Matrix, perform column-wise concatenation of strings, handling variable lists lengths.
def ver_con(mat1):
    res = []
    for i in range(len(mat1)):
        temp = ''
        for r in mat1:
            try: temp += r[i]
            except IndexError: pass
        res.append(temp)
    return res


if __name__ == "__main__":
    row = int(input("Enter number of rows"))
    print("Enter the string matrix elements:")
    mat = [list(input().split(" ")) for i in range(row)]
    print("Vertical Concatenation:", ver_con(mat))
