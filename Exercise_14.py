def deduplicate(List):
    s = set(List)
    l = list(s)
    return l

def deduplicate_1(List):
    s = set()
    for element in List:
        s.add(element)
    l = list(s)
    return l

def deduplicate_2(List):
    l = []
    for element in List:
        if element not in l:
            l.append(element)
    return l

values = [1, 3, 5, 7, 9, 7, 5, 3, 1]
print(deduplicate(values))
print(deduplicate_1(values))
print(deduplicate_2(values))
