a = list(range(0, 101, 5))
print(a)
b = list(range(0, 51, 2))
print(b)
a1 = len(a)
b1 = len(b)
c = []
if a1 <= b1:
    for number in b:
        if number in a:
            c.append(number)
if a1 > b1:
    for number in a:
        if number in b:
            c.append(number)
print(c)
