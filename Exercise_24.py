def board():
    size = int(input("How many rows and columns do you want your board to have? "))
    count = 0
    while count < size:
        print(" --- " * size)
        print("|   |" * size)
        count = count + 1
    print(" --- " * size)

board()
