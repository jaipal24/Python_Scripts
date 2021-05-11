# Area of a circle can simply be evaluated using following formula.
# Area = pi * r2
# where r is radius of circle

def circle_area(r):
    PI=3.14
    return PI * pow(r, 2)


if __name__ == "__main__":
    rad = int(input("Enter Radius of the Circle:"))
    res = circle_area(rad)
    print(res)
