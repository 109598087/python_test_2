from itertools import product, permutations

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

all_comb = list(permutations([i for i in range(N)]))
print(all_comb)

