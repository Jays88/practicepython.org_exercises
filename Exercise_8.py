"""
This is my attempt at creating a program who would let 2 players play the 'Rock Paper Scissors' game among themselves.
Author: Janek Krikava
"""
from time import sleep

print("Hey! Hey! Hey! Take it easy man. Over here!")
sleep(2)
print("There is a pile of rocks waiving at you.")
sleep(2)
print("Allow me to introduce myself. My name is Korg and I am kind of like the leader in here.\nI am made of rocks but don't let that intimidate you. You don't need to be afraid. ")
sleep(2)
print("Unless you are made of scissors, of course!")
sleep(2)
print("That was a little Rock Paper Scissors joke for ya")
sleep(2)
print("")
def game():
    player_a = input("There is a game I like to play with my friend Meek over here, do you want to try it? Please answer either 'Yes' or 'No'. ")
    player_a = player_a.lower()
    if player_a == "yes":
        print(yeah())
    elif player_a == "no":
        print(sorry())
    else:
        print(dumb_ass())
def dumb_ass():
    print("")
    print("You are not capable of playing if you can't choose neither of the two proposed options because this game offers you 3 options.")
    print("Please come back when you unlock the 'decision making' skill from your skills tree")

def sorry():
    print("")
    print("Sorry, you need to have a buddy to play this game.")
    print("Maybe try it next time when you are not alone")

def yeah():
    player_2 = input("Do you have another player to play the game with you? Please answer either 'Yes' or 'No': ")
    player_2 = player_2.lower()
    print("")
    if player_2 == "yes":
        print("")
        print("Let's bring it on!")
        print(game_1())
    elif player_2 == "no":
        print(sorry())
    else:
        print(dumb_ass())

def play_again():
    q = input("Do you want to play again? Please answer 'Yes' or 'No': ")
    q = q.lower()
    if q == "yes":
        result = True
    elif q == "no":
        result = False
    else:
        print(dumb_ass())

def game_1():
    name_1 = str(input("Please state your name: "))
    name_2 = str(input("Now may the other player state his/her name: "))
    result = True
    while result == True:
        guess_1 = input(name_1 + ", Please tell the other player to turn around and pick your weapon of choice: Is it going to be 'Rock', 'Paper', or 'Scissors'? ")
        guess_1 = guess_1.lower()
        guess_2 = input(name_2 + ", Please tell" + name_1 + " to turn around and pick your weapon of choice: Is it going to be 'Rock, 'Paper', or 'Scissors'? ")
        guess_2 = guess_2.lower()
        if ((guess_1 == "rock" and guess_2 == "scissors") or (guess_1 == "scissors" and guess_2 == "paper") or (guess_1 == "paper" and guess_2 == "rock")):
            print("Congratulations, ", name_1,"! You have won this round")
            print(play_again())
        elif ((guess_2 == "rock" and guess_1 == "scissors") or (guess_2 == "scissors" and guess_1 == "paper") or (guess_2 == "paper" and guess_1 == "rock")):
            print("Congratulations, ", name_2,"! You have won this round")
            print(play_again())
        elif guess_1 == guess_2:
            print("It is a tie. Please try again.")
            print("")
        else:
            print("So you can decide between 2 options but 3 is too much? One of you needs to invest a bit more development points in your 'decision making' skill. Now get lost")
            result = False
            
print(game())
