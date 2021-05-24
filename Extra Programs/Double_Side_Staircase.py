if __name__ == "__main__":
    n = int(input("Enter size:"))
    for i in range(1, n+1):
        st = (n-i) * "  " + i * "* " + i * "* " + (n-i) * "  "
        print(st)
        print(st)
