def reverse(words):
    split = words.split()
    l = int(len(split))
    r = split[l-1::-1]
    n = " ".join(r)
    return n

something = str(input("Please enter a phrase consisiting of multiple words: "))
print(reverse(something))
