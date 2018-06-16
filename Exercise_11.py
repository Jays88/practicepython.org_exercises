number = int(input("Please enter a number: "))
if number < 0:
    number = number * (-1)
count = 1
numbers = []
while count <= number:
    if number >= 0 and number < 2:
        print(number, "can only be divided by itself")
    elif number % count == 0:
        numbers.append(count)
    count = count + 1

a = len(numbers)
if a == 2:
    print("The number you entered is a prime number")
else:
    print("The number you entered is not a prime number")
