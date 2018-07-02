from random import choice
lines = []
def word():
    with open('sowpods.txt', 'r') as f:
        line = f.readline().strip()
        while line:
            lines.append(line)
            line = f.readline().strip()
    return print(choice(lines))

word()
