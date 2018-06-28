def maximum(x, y, z):
    high = 0
    if (a > b and a > c):
        high = a
    elif (b > a and b > c):
        high = b
    elif (c > a and c > b):
        high = c
    return print(high)
a = int(input("Please insert a number: "))
b = int(input("Please insert a second number: "))
c = int(input("Please insert the last number: "))
maximum(a, b, c)
