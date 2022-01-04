import copy
from itertools import product, permutations


def get_all_classroom_comb_list(classroom_list, class_number):
    a = copy.deepcopy(classroom_list)
    a = [[num for num in comb] for comb in list(product(a, classroom_list))]
    b = copy.deepcopy(a)
    for i in range(class_number - 2):
        b = [comb[0] + [comb[1]] for comb in list(product(b, classroom_list))]
    return b


def is_time_ok(start_time, end_time, classroom_time_dict):
    for remove_time in range(start_time, end_time + 1):
        if remove_time not in classroom_time_dict[classroom]:
            return False
    return True


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

# for class_comb in all_class_comb_list:
#     for classroom_comb in all_classroom_comb_list:
classroom_time_dict = {key: [i + 1 for i in range(24)] for key in classroom_dict}

print(classroom_time_dict)
print(all_class_comb_list[0])
print(all_classroom_comb_list[0])

time = 0
result_class_classroom = list()
for i in range(len(all_class_comb_list[0])):
    _class = all_class_comb_list[0][i]
    classroom = all_classroom_comb_list[0][i]

    class_people = class_dict[_class][0]
    start_time = class_dict[_class][1]
    end_time = class_dict[_class][2]
    classroom_people = classroom_dict[classroom]
    if class_people <= classroom_people and is_time_ok(start_time, end_time, classroom_time_dict):
        time += end_time - start_time
        result_class_classroom.append([_class, classroom])
        for remove_time in range(start_time, end_time + 1):
            classroom_time_dict[classroom][classroom_time_dict[classroom].index(remove_time)] = 0
        print(classroom_time_dict)
print(time)
print(result_class_classroom)
