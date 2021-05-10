# Given two numbers, write a Python code to find the Maximum of these two numbers.
def max_value(a, b):
    if a >= b:
        return a
    else:
        return b


if __name__ == "__main__":
    num1 = input("Enter First Number:")
    num2 = input("Enter Second Number:")
    res = max_value(int(num1), int(num2))
    print(res)
