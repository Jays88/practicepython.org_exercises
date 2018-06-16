number = int(input("Please specify how many long do you want your Fibonacci sequence to be: "))
count = 1
a = 0
b = 1
fib = [1]
while count < number:
    c = a + b
    fib.append(c)
    a = b
    b = c
    count = count + 1
print(fib)
