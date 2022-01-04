from itertools import product, permutations, combinations

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
print()

class_permutation = list(permutations([key for key in class_dict.keys()]))
print(class_permutation)
classroom_time_dict = {key: [i + 1 for i in range(24)] for key in classroom_dict.keys()}

