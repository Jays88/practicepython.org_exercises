from time import sleep 
import random

def letters():
    p = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    random.shuffle(p)
    let = 0
    l = []
    while let < toughness:
        l.append(p[random.randint(0, 9)])
        let = let + 1
    return l

def LETTERS():
    p = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    p = [x.upper() for x in p]
    random.shuffle(p)
    let = 0
    l = []
    while let < toughness:
        l.append(p[random.randint(0, 9)])
        let = let + 1
    return l

def numbers():
    n = []
    for i in range (0, toughness):
        n.append(random.randint(0,9))
    return n

def symbols():
    s = ["£", "$", "&", "*", "?", "/", "#"] 
    random.shuffle(s)
    let = 0
    l = []
    while let < toughness:
        l.append(s[random.randint(0, 6)])
        let = let + 1
    return l

def difficulty():
    dif = str(input("Please specify how strong you want your password to be - easy, medium, or hard?: "))
    dif = dif.lower()
    while True:
        if dif == "easy":
            return 1
        elif dif == "medium":
            return 2
        elif dif == "hard":
            return 3
        else:
            print("please run the program again, you wrote a typo.")
            exit(difficulty)

def password():
    pword = symbols() + letters() + LETTERS() + numbers()
    random.shuffle(pword)
    print("Please not down the phrase below. This is your new password")
    return pword

toughness = difficulty()
print(password())
