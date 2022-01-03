from itertools import product, permutations

M = int(input())
N = int(input())
print(list(permutations([0, 1, 2, 3, 4])))
classroom_dict = dict()
for _ in range(M):
    classroom_split = input().split(' ')
    classroom_dict[classroom_split[0]] = classroom_split[1]
print(classroom_dict)


class_dict = dict()
for _ in range(N):
    class_split = input().split(' ')
    class_dict[class_split[0]] = [class_split[1], class_split[2], class_split[3]]

print(class_dict)
