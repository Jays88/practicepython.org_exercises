counter = 1
import random
number = random.randint(1,9)
guess = int(input("Please enter a number between 1 and 9: "))
while guess != number:
    if guess > number:
        print("That is a bit too high. Try to guess a lower number")
    elif guess < number:
        print("That is a bit too low. Try to guess a higher number")
    else:
        print("Congratulations. You guessed it!")
        print("")
        break
    counter = counter + 1
    guess = int(input("Please enter a different number: "))
counter = int(counter)
print("It took you", counter, "attempts")
