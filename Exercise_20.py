numbers = [1, 4, 6, 7, 90, 23, 56, 84, 93, 11, 21, 26, 48, 56, 72, 59, 12, 18, 86, 79, 48]
def check(List, number):
    dedup = []
    for element in List:
        if element not in dedup:
            dedup.append(element)
    dedup.sort()
    if number in dedup:
        return print(number," is in the list of numbers")
    else:
        return print(number," is not in the list of numbers")
guess = int(input("Please insert a number you want to check against a list: "))
check(numbers, guess)
