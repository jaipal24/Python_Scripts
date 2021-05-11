# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100
# Where,
# P is the principle amount
# T is the time and
# R is the rate

if __name__ == "__main__":
    P = float(input("Enter Principle amount:"))
    R = float(input("Enter rate of interest:"))
    T = float(input("Enter time period:"))
    res = (P * T * R)/100
    print(round(res, 2))
