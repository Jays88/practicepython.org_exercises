winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
def winner(outcome):
    #Player 2
    if (outcome[0][0] == 2 and outcome[1][0] == 2 and outcome[2][0] == 2):
        return print("Player 2 won this round")
    elif (outcome[0][0] == 2 and outcome[0][1] == 2 and outcome[0][2] == 2):
        return print("Player 2 won this round")
    elif (outcome[0][0] == 2 and outcome[1][1] == 2 and outcome[2][2] == 2):
        return print("Player 2 won this round")
    elif (outcome[1][0] == 2 and outcome[1][1] == 2 and outcome[1][2] == 2):
        return print("Player 2 won this round")
    elif (outcome[2][0] == 2 and outcome[2][1] == 2 and outcome[2][2] == 2):
        return print("Player 2 won this round")
    elif (outcome[0][1] == 2 and outcome[1][1] == 2 and outcome[2][1] == 2):
        return print("Player 2 won this round")
    elif (outcome[0][2] == 2 and outcome[1][2] == 2 and outcome[2][2] == 2):
        return print("Player 2 won this round")
    elif (outcome[0][2] == 2 and outcome[1][1] == 2 and outcome[2][0] == 2):
        return print("Player 2 won this round")
    #Player 1
    elif (outcome[0][0] == 1 and outcome[1][0] == 1 and outcome[2][0] == 1):
        return print("Player 1 won this round")
    elif (outcome[0][0] == 1 and outcome[0][1] == 1 and outcome[0][2] == 1):
        return print("Player 1 won this round")
    elif (outcome[0][0] == 1 and outcome[1][1] == 1 and outcome[2][2] == 1):
        return print("Player 1 won this round")
    elif (outcome[1][0] == 1 and outcome[1][1] == 1 and outcome[1][2] == 1):
        return print("Player 1 won this round")
    elif (outcome[2][0] == 1 and outcome[2][1] == 1 and outcome[2][2] == 1):
        return print("Player 1 won this round")
    elif (outcome[0][1] == 1 and outcome[1][1] == 1 and outcome[2][1] == 1):
        return print("Player 1 won this round")
    elif (outcome[0][2] == 1 and outcome[1][2] == 1 and outcome[2][2] == 1):
        return print("Player 1 won this round")
    elif (outcome[0][2] == 1 and outcome[1][1] == 1 and outcome[2][0] == 1):
        return print("Player 1 won this round")
    #Tie
    else:
        return print("It's a tie! Nobody wins.")

winner(winner_is_2)
