# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
# Fn = Fn-1 + Fn-2
# With seed values
# F0 = 0 and F1 = 1.

def fibonacci(val):
    if val < 0:
        print("Incorrect Input!!")
    elif val == 1:
        return 0
    elif val == 2:
        return 1
    else:
        return fibonacci(val-1)+fibonacci(val-2)


if __name__ == "__main__":
    n = int(input("Enter a number"))
    res = fibonacci(n)
    print(res)
