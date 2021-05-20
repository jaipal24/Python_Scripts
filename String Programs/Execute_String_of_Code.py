# Given few lines of code inside a string variable and execute the code inside the string.
def exec_code():
    s = """
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print(factorial(5))
"""
    exec(s)


if __name__ == "__main__":
    exec_code()
