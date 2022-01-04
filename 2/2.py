# from itertools import product, permutations, combinations
#
# row1_split = input().split(' ')
# M = int(row1_split[0])
# N = int(row1_split[1])
#
# classroom_dict = dict()
# for _ in range(M):
#     classroom_split = input().split(' ')
#     classroom_dict[classroom_split[0]] = int(classroom_split[1])
# print(classroom_dict)
#
# class_dict = dict()
# for _ in range(N):
#     class_split = input().split(' ')
#     class_dict[class_split[0]] = [int(class_split[1]), int(class_split[2]), int(class_split[3])]
# print(class_dict)
#
# class_permutation = list(permutations([key for key in class_dict.keys()]))
# print(class_permutation)
# classroom_time_dict = {key: [i + 1 for i in range(24)] for key in classroom_dict.keys()}
#
# print(list(combinations(classroom_dict.keys(), 2)))
from itertools import combinations, permutations

from itertools import combinations

print(set(list(permutations([1102, 1102, 1102, 2103], 4))))
# for


# print(classroom_time_dict)

# for class_index in class_permutation[0]:
#     class_dict
