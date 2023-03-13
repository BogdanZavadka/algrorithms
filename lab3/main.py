pairs = ['1 2', '2 4', '1 3', '3 5', '8 10', '10 11', '8 9', '12 15', '15 16']


def search_values_int_string(pair: str) -> [int]:
    first_number = ''
    k = 0
    while pair[k] != ' ':
        first_number += pair[k]
        k += 1
    second_number = pair[k + 1:]
    return [int(first_number), int(second_number)]


def sort_by_tribes(pairs):
    tribe_index = -1
    tribes = []
    for i in pairs:
        numbers = search_values_int_string(i)
        if pairs.index(i) == 0:
            tribes.append(numbers)
        else:
            for j in tribes:
                if numbers[0] in j:
                    tribe_index = tribes.index(j)
            if tribe_index == -1:
                tribes.append(numbers)
            else:
                tribes[tribe_index].append(numbers[1])
            tribe_index = -1
    return tribes


def find_pairs(tribes):
    result = []
    boys = []
    girls = []
    for i in tribes:
        girls_of_one_tribe = []
        boys_of_one_tribe = []
        for j in i:
            if j % 2 == 0:
                girls_of_one_tribe.append(j)
            else:
                boys_of_one_tribe.append(j)
        boys.append(boys_of_one_tribe)
        girls.append(girls_of_one_tribe)
    for i in girls:
        for girl in i:
            for k in boys:
                if girls.index(i) != boys.index(k):
                    for boy in k:
                        result.append(f'{boy}/{girl}')
    print('All possible pairs:')
    print(*result)


tribes = sort_by_tribes(pairs)
find_pairs(tribes)
