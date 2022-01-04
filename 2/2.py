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
    for remove_time in range(start_time, end_time):
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
# print(classroom_dict)

class_dict = dict()
for _ in range(N):
    class_split = input().split(' ')
    class_dict[class_split[0]] = [int(class_split[1]), int(class_split[2]), int(class_split[3])]
# print(class_dict)

all_classroom_comb_list = get_all_classroom_comb_list(list(classroom_dict.keys()), len(list(class_dict.keys())))
# print(all_classroom_comb_list)

all_class_comb_list = list(permutations(list(class_dict.keys())))
# print(all_class_comb_list)

time_list = list()
all_comb_result_class_classroom_list = list()
for class_comb in all_class_comb_list:
    for classroom_comb in all_classroom_comb_list:
        classroom_time_dict = {key: [i + 1 for i in range(24)] for key in classroom_dict}
        time = 0
        result_class_classroom = list()

        for i in range(len(class_comb)):
            _class = class_comb[i]
            classroom = classroom_comb[i]

            class_people = class_dict[_class][0]
            start_time = class_dict[_class][1]
            end_time = class_dict[_class][2]
            classroom_people = classroom_dict[classroom]
            # 如果教室有空位，時間也可以 -> 加入
            if class_people <= classroom_people and is_time_ok(start_time, end_time, classroom_time_dict):
                time += end_time - start_time
                result_class_classroom.append([_class, classroom])
                for remove_time in range(start_time, end_time):
                    classroom_time_dict[classroom][classroom_time_dict[classroom].index(remove_time)] = 0
            # print(classroom_time_dict)
        time_list.append(time)
        all_comb_result_class_classroom_list.append(result_class_classroom)
        # print(time)
        # print(result_class_classroom)

# print(time_list)
# print(all_comb_result_class_classroom_list)

class_number_list = [len(result) for result in all_comb_result_class_classroom_list]
# print(class_number_list)

# max time
max_time = max(time_list)
print(max_time)
for i in range(len(time_list)):
    if time_list[i] == max_time:
        print(time_list[i], all_comb_result_class_classroom_list[i])

# max class number
max_class_number = max(class_number_list)
print(max_class_number)
for i in range(len(class_number_list)):
    if class_number_list[i] == max_class_number:
        print(all_comb_result_class_classroom_list[i])
