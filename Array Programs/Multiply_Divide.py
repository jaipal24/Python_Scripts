# Given multiple numbers and a number n,
# the task is to print the remainder after multiply all the number divide by n.

if __name__ == "__main__":
    arr = map(int, input("Enter array elements:").split(" "))
    n = int(input("Enter number to divide:"))
    val = 1
    for i in arr:
        val = val * i
    print(round(val/n, 2))
