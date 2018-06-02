palindrom = list(input("Please enter a random word: "))
number = int(len(palindrom))
half = int(number / 2)
remainder = number % 2
if remainder == 0:
    a = (palindrom[:half])
    half = half - 1
    b = (palindrom[number:half:-1])
    if a == b:
        print("The word you have entered is a palindrome")
    else:
        print("The word you have entered is not a palindrome")
else:
    a = (palindrom[:half])
    b = (palindrom[number:half:-1])
    if a == b:
        print("The word you have entered is a palindrome")
    else:
        print("The word you have entered is not a palindrome")
