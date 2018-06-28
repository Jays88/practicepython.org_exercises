game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def intro():
    print("Player 1 will be represented by 'X'.")
    print("Player 2 will be represented by 'O'.")

def player_1(table):
    pos = input(str("Player 1, please enter where you want your next move to be using format \"row *gap* col\": "))
    print(pos)
    pos_list = pos.split(" ")
    print(pos_list)
    if (pos_list[0] == "1" and pos_list[1] == "1"):
        table[0][0] = "X"
        print(table)
    elif (pos_list[0] == "2" and pos_list[1] == "1"):
        table[1][0] = "X"
        print(table)
    elif (pos_list[0] == "3" and pos_list[1] == "1"):
        table[2][0] = "X"
        print(table)
    elif (pos_list[1] == "1" and pos_list[0] == "2"):
        table[0][1] = "X"
        print(table)
    elif (pos_list[0] == "1" and pos_list[1] == "3"):
        table[0][2] = "X"
        print(table)
    elif (pos_list[0] == "2" and pos_list[1] == "2"):
        table[1][1] = "X"
        print(table)
    elif (pos_list[0] == "2" and pos_list[1] == "3"):
        table[1][2] = "X"
        print(table)
    elif (pos_list[0] == "3" and pos_list[1] == "2"):
        table[2][1] = "X"
        print(table)
    elif (pos_list[0] == "3" and pos_list[1] == "3"):
        table[2][2] = "X"
        print(table)
    return table

def player_2(table):
    pos = input(str("Player 2, please enter where you want your next move to be using format \"row *gap* col\": "))
    print(pos)
    pos_list = pos.split(" ")
    print(pos_list)
    if (pos_list[0] == "1" and pos_list[1] == "1"):
        table[0][0] = "O"
        print(table)
    elif (pos_list[0] == "2" and pos_list[1] == "1"):
        table[1][0] = "O"
        print(table)
    elif (pos_list[0] == "3" and pos_list[1] == "1"):
        table[2][0] = "O"
        print(table)
    elif (pos_list[1] == "1" and pos_list[0] == "2"):
        table[0][1] = "O"
        print(table)
    elif (pos_list[0] == "1" and pos_list[1] == "3"):
        table[0][2] = "O"
        print(table)
    elif (pos_list[0] == "2" and pos_list[1] == "2"):
        table[1][1] = "O"
        print(table)
    elif (pos_list[0] == "2" and pos_list[1] == "3"):
        table[1][2] = "O"
        print(table)
    elif (pos_list[0] == "3" and pos_list[1] == "2"):
        table[2][1] = "O"
        print(table)
    elif (pos_list[0] == "3" and pos_list[1] == "3"):
        table[2][2] = "O"
        print(table)
    return table

def tic_tac(table):
    counter = 0
    while counter < 4:
        player_1(table)
        player_2(table)
        counter = counter + 1
    player_1(table)
    return table

intro()
tic_tac(game)
