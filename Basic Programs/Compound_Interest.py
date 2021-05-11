# Formula to calculate compound interest annually is given by:
# A = P(1 + R/100)^t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span

if __name__ == "__main__":
    P = float(input("Enter principle amount:"))
    T = float(input("Enter time span:"))
    R = float(input("Enter rate of interest:"))
    A = P * pow((1 + R/100), T)
    res = A - P
    print(round(res, 2))
