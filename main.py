import math

def rad_to_deg(theta):
    return theta * (180 / math.pi)

def to_imaginary_polar(r, theta):
    return f"{r}cis({theta})"

def to_polar(x, y):
    r = math.sqrt( (x**2 + y**2) )

    try:
        tan = y / x;
    except ZeroDivisionError:
        tan = math.pi/2;

    theta = math.atan(tan);

    return r, theta


print(to_polar(5,5))

r, theta = to_polar(3,4)

print(to_imaginary_polar(r, rad_to_deg(theta)))