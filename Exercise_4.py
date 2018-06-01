a = int(input("Please enter a number:"))
count = 1
print("You have just entered the number:", a)
length = list()

while count <= a:
    if a == 0:
        print("You cannot divide with number 0")
    elif a % count == 0:
        length.append(count)
    elif a % count != 0:
        print("The number", count,"is not a divisor of number",a)
    count = count + 1
print("The following numbers are divisors of number", a,":", length)
