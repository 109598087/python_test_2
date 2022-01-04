import copy
from itertools import product


def get_all_classroom_comb_list(classroom_list, class_number):
    # classroom_list = ['2011', '1123']
    a = copy.deepcopy(classroom_list)

    a = [[num for num in comb] for comb in list(product(a, classroom_list))]

    b = copy.deepcopy(a)
    for i in range(class_number - 2):
        b = [comb[0] + [comb[1]] for comb in list(product(b, classroom_list))]
    return b


all_classroom_comb_list = get_all_classroom_comb_list(['2011', '1123'], 4)
print(all_classroom_comb_list)
