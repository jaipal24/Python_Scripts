if __name__ == "__main__":
    n = int(input("Enter the size:"))
    for i in range(0, n):
        st = i * " " + (n-i) * "*"
        print(st)
