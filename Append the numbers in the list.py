numbers = [2, 2, 4, 5, 6, 7, 8, 9, 10]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)