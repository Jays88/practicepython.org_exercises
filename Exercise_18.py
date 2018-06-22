import random
from time import sleep
def welcome():
    sleep(1)
    print("This is how the game works: ")
    sleep(1)
    print("\t* A random 4 digit number is generated\n\t* You will be prompt to guess the number\n\t* Every time you guess a number which is in the mysterious number, you receive 1 bull.\n* Examples: \n\t\t* Let's say that the random number is 1234. If your guess is 1548, you will get 1 cow and 2 bulls because you managed to guess 2 numbers which are there ('1' and '4'). Additionally, you will get 1 cow because you guessed the right position of one of those numbers (number '1').\n\t\t* In a different example, where the random number stays 1234, if your guess is 1111, you will get 1 cow and 4 bulls. The reason for is that all the numbres you guessed are in the mysterious number, giving you 4 bulls. And because one of the '1' you guessed is in the right place, it gives you 1 cow.\n\t* Additionally, if you guess both rhe number and the place, you get 1 cow\n\t* If you guess no number correctly, you get nothing\n\t* Your aim should be to guess the number (and get 4 cows and 4 bulls) in as few attempts as possible")
    sleep(10)
    while True:
        q = str(input("Everything clear? Please answer either 'yes' or 'no': "))
        q = q.lower()
        if (q == "yes" or q == "y"):
            return print("Great! Let's get to it...\n")
        elif (q == "no" or q == "n"):
            return print("That's a shame... Maybe read the instructions again\n"), welcome(), sleep(1)
        else:
            print("Please try again. You mistyped the answer\n"), sleep(1)

def number():
    n = random.randint(1000, 9999)
    return n

def guess():
    print("Take a guess\n")
    while True:
        guess = int(input("Please enter a 4 digit number which doesn't start with '0': "))
        l = len(str(guess))
        if l != 4:
            return print("Please try again and this time, entere a 4 digit number.\n"), sleep(1)
        else:
            return guess

def game():
    print("Carry on guessing until you have 4 cows.")
    sleep(2)
    print("There is 1 in 8999 chance that you will guess the correct number on your first attempt. Let's see if today is your lucky day")
    sleep(3)
    cow = 0
    bull = 0
    count = 0
    attempts = 0
    ran_num_int = number()
    ran_num_str = str(ran_num_int)
    ran_num_list = list(ran_num_str[0:4])
    while cow != 4:
        input_num_int = guess()
        print("Your number is", input_num_int)
        input_num_str = str(input_num_int)
        input_num_list = list(input_num_str[0:4])
        sleep(1)
        a = ran_num_list
        b = input_num_list
        count = 0
        while count < 4:
            if a[count] == b[count]:
                cow = cow + 1
            count += 1
        for element in b:
            if element in a:
                bull = bull + 1
        print("Cow: ", cow,"; Bull: ", bull,"\n")
        if cow !=4:
            cow = 0
            bull = 0
            attempts = attempts + 1
        elif cow == 4:
            print("Well done")
            print("The random number was", ran_num_int)
            sleep(3)
            attempts = attempts + 1
    return print("It has taken you", attempts," attempts to guess the number")

print("Welcom to the game of 'Bulls & Cows'\n")
welcome()
print("Let's find out how many cows and bulls will this guess get you, shall we?\n")
sleep(2)
game()
