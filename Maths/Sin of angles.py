from numpy import sin, deg2rad

sin3deg = sin(deg2rad(3))


def f(x):
    return (sin3deg + 4 * x ** 3) / 3


x = sin3deg / 3
for i in range(5):
    x = f(x)
    print(x)