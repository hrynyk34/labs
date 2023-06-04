from itertools import combinations

def select(list_1, list_2):
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    counter = 0
    numbers = list_1 + list_2
    pairs = []
    for pair in combinations(numbers, 2):
        if sum(pair) == 10:
            pairs.append(pair)

    if len(pairs) > 0:
        print('Ваші числа, сума яких рівна 10:')
        for pair in pairs:
            print(pair[0], pair[1])
    else:
        print('Немає чисел, сума яких рівна 10.')

select([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9])
