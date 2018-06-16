def last_and_first(a_list):
    al = len(a_list)
    b = [a_list[0], a_list[al - 1]]
    return b
a = [5, 10, 15, 20, 25]
print(last_and_first(a))
