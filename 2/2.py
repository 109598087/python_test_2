import copy
from itertools import product, permutations


def get_all_classroom_comb_list(classroom_list, class_number):
    a = copy.deepcopy(classroom_list)
    a = [[num for num in comb] for comb in list(product(a, classroom_list))]
    b = copy.deepcopy(a)
    for i in range(class_number - 2):
        b = [comb[0] + [comb[1]] for comb in list(product(b, classroom_list))]
    return b


row1_split = input().split(' ')
M = int(row1_split[0])
N = int(row1_split[1])

classroom_dict = dict()
for _ in range(M):
    classroom_split = input().split(' ')
    classroom_dict[classroom_split[0]] = int(classroom_split[1])
print(classroom_dict)

class_dict = dict()
for _ in range(N):
    class_split = input().split(' ')
    class_dict[class_split[0]] = [int(class_split[1]), int(class_split[2]), int(class_split[3])]
print(class_dict)

all_classroom_comb_list = get_all_classroom_comb_list(list(classroom_dict.keys()), len(list(class_dict.keys())))
print(all_classroom_comb_list)

all_class_comb_list = list(permutations(list(class_dict.keys())))
print(all_class_comb_list)

for class_comb in all_class_comb_list:
    for classroom_comb in all_classroom_comb_list:
