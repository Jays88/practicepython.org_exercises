from time import sleep

def intro():
    print("Welcome to the game of 'Tic Tac Toe'!!!")
    sleep(1)
    print("The goal is simple. You will be playing against each other and whoever will connect 3 symbols either in a row, or a column, or diagonally will win the game.")
    sleep(2)
    print("Player 1 will be represented by 'X'.")
    print("Player 2 will be represented by 'O'.")
    count = 0
    while count < 1:
        ready = str(input("Are you ready to have fun and start the game? Answer please either 'Yes' or 'No': "))
        ready = ready.lower()
        if (ready == "yes" or ready == 'y'):
            print("Alrighty then!\n")
            sleep(1)
            count = count + 1
        elif (ready == "no" or ready == 'n'):
            print("In that case, please open the file once you are ready.")
            sleep(2)
            exit()
        else:
            print("Maybe you want to try again and type the answer corretly.")
            sleep(1)
    
def board():
    count = 0
    size = 3
    while count < size:
        print(" --- " * size)
        print("|   |" * size)
        count = count + 1
    print(" --- " * size)

def board_1(table):
    print(" ---  ---  --- ")
    print("|",table[0][0],"||",table[0][1],"||",table[0][2],"|")
    print(" ---  ---  --- ")
    print("|",table[1][0],"||",table[1][1],"||",table[1][2],"|")
    print(" ---  ---  --- ")
    print("|",table[2][0],"||",table[2][1],"||",table[2][2],"|")
    print(" ---  ---  --- ")

def winner(table):
    #Player 2
    if (table[0][0] == "O" and table[1][0] == "O" and table[2][0] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[0][0] == "O" and table[0][1] == "O" and table[0][2] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[0][0] == "O" and table[1][1] == "O" and table[2][2] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[1][0] == "O" and table[1][1] == "O" and table[1][2] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[2][0] == "O" and table[2][1] == "O" and table[2][2] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[0][1] == "O" and table[1][1] == "O" and table[2][1] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[0][2] == "O" and table[1][2] == "O" and table[2][2] == "O"):
        print("Player 2 won this round")
        return 2
    elif (table[0][2] == "O" and table[1][1] == "O" and table[2][0] == "O"):
        print("Player 2 won this round")
        return 2
    
    #Player 1
    elif (table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[0][0] == "X" and table[0][1] == "X" and table[0][2] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[1][0] == "X" and table[1][1] == "X" and table[1][2] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[2][0] == "X" and table[2][1] == "X" and table[2][2] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "X"):
        print("Player 1 won this round")
        return 1
    elif (table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X"):
        print("Player 1 won this round")
        return 1
    #Tie
    else:
        print("It's a tie! Nobody wins.")
        return 0
def player_1(table):
    pos = input(str("Player 1, please enter where you want your next move to be using format \"row *gap* col\": "))
    pos_list = pos.split(" ")
    if (pos_list[0] == "1" and pos_list[1] == "1" and table[0][0] == " "):
        table[0][0] = "X"
    elif (pos_list[0] == "2" and pos_list[1] == "1" and table[1][0] == " "):
        table[1][0] = "X"
    elif (pos_list[0] == "3" and pos_list[1] == "1" and table[2][0] == " "):
        table[2][0] = "X"
    elif (pos_list[0] == "1" and pos_list[1] == "2" and table[0][1] == " "):
        table[0][1] = "X"
    elif (pos_list[0] == "1" and pos_list[1] == "3" and table[0][2] == " "):
        table[0][2] = "X"
    elif (pos_list[0] == "2" and pos_list[1] == "2" and table[1][1] == " "):
        table[1][1] = "X"
    elif (pos_list[0] == "2" and pos_list[1] == "3" and table[1][2] == " "):
        table[1][2] = "X"
    elif (pos_list[0] == "3" and pos_list[1] == "2" and table[2][1] == " "):
        table[2][1] = "X"
    elif (pos_list[0] == "3" and pos_list[1] == "3" and table[2][2] == " "):
        table[2][2] = "X"
    else:
        print("You either ran out of space and put your cross outside of the table or you tried to put your cross in a spot which is already full. Try again"), player_1(table)
    return table

def player_2(table):
    pos = input(str("Player 2, please enter where you want your next move to be using format \"row *gap* col\": "))
    pos_list = pos.split(" ")
    if (pos_list[0] == "1" and pos_list[1] == "1" and table[0][0] == " "):
        table[0][0] = "O"
    elif (pos_list[0] == "2" and pos_list[1] == "1" and table[1][0] == " "):
        table[1][0] = "O"
    elif (pos_list[0] == "3" and pos_list[1] == "1" and table[2][0] == " "):
        table[2][0] = "O"
    elif (pos_list[0] == "1" and pos_list[1] == "2" and table[0][1] == " "):
        table[0][1] = "O"
    elif (pos_list[0] == "1" and pos_list[1] == "3" and table[0][2] == " "):
        table[0][2] = "O"
    elif (pos_list[0] == "2" and pos_list[1] == "2" and table[1][1] == " "):
        table[1][1] = "O"
    elif (pos_list[0] == "2" and pos_list[1] == "3" and table[1][2] == " "):
        table[1][2] = "O"
    elif (pos_list[0] == "3" and pos_list[1] == "2" and table[2][1] == " "):
        table[2][1] = "O"
    elif (pos_list[0] == "3" and pos_list[1] == "3" and table[2][2] == " "):
        table[2][2] = "O"
    else:
         print("You either ran out of space and put your circle outside of the table or you tried to put your circle in a spot which is already full. Try again"), player_2(table)
    return table

def tic_tac(table):
    counter = 0
    while counter < 4:
        player_1(table)
        board_1(table)
        sleep(1)
        player_2(table)
        board_1(table)
        sleep(1)
        counter = counter + 1
    player_1(table)
    board_1(table)
    return table

def again():
    table = print("This is the board you will be playing at"), board()
    sleep(2)
    tic_tac(game)
    sleep(2)
    p1_win = 0
    p2_win = 0
    ties = 0
    if winner(game) == 1:
        p1_win = p1_win + 1
    elif winner(game) == 2:
        p2_win = p2_win + 1
    else:
        ties = ties + 1
    q = str(input("Do you want to play again? Please answer 'Yes' or 'No': "))
    q = q.lower()
    if (q == "yes" or q == "y"):
        print("The current score is:\n\tPlayer 1 won", p1_win," times\n\tPlayer 2 won", p2_win," times\n\tThe game ended", ties," times in a tie\n")
        sleep(3)
        again()
    else:
        print("Thank you for playing!")
        print("Player 1 won", p1_win," times.")
        print("Player 2 won", p2_win," times.")
        print("The game ended in a draw", ties," times.")
        print("Have a nice day!")
        sleep(2)
        exit()

game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
intro()
table = print("This is the board you will be playing at"), board()
sleep(2)
tic_tac(game)
sleep(2)
winner(game)
p1_win = 0
p2_win = 0
ties = 0
if winner == "Player 1 won this round":
    p1_win = p1_win + 1
elif winner == "Player 2 won this round":
    p2_win = p2_win + 1
else:
    ties = ties + 1
game = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
q = str(input("This was a warm-up round. Do you want to play again and start counting your wins? Please answer 'Yes' or 'No': "))
q = q.lower()
if (q == "yes" or q == "y"):
    again()
else:
    print("Thank you for playing! Have a nice day.")
    exit()
