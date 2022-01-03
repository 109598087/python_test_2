import copy

row1 = input()
# try:
M = int(row1.split(' ')[0])
N = int(row1.split(' ')[1])
print('OK')
# except:
# print('Error')

start_game = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

player1_list = list()
player2_list = list()
for i in range(N):
    row = input()
    row_split = row.split(' ')
    player1_list.append(int(row_split[0]))
    player2_list.append(int(row_split[1]))


# print(player1_list)
# print(player2_list)


def into_game(num, start_game, player_computer):
    if num == 1:
        start_game[0][0] = player_computer
    elif num == 2:
        start_game[0][1] = player_computer
    elif num == 3:
        start_game[0][2] = player_computer
    elif num == 4:
        start_game[1][0] = player_computer
    elif num == 5:
        start_game[1][1] = player_computer
    elif num == 6:
        start_game[1][2] = player_computer
    elif num == 7:
        start_game[2][0] = player_computer
    elif num == 8:
        start_game[2][1] = player_computer
    elif num == 9:
        start_game[2][2] = player_computer
    else:
        print('Error')
    return start_game


# add
if M == 1:
    for num in player1_list:
        start_game = into_game(num, start_game, 1)
    for num in player2_list:
        start_game = into_game(num, start_game, 2)
else:
    for num in player1_list:
        start_game = into_game(num, start_game, 2)
    for num in player2_list:
        start_game = into_game(num, start_game, 1)

# 2 3 4 行
for i in range(len(start_game)):
    for num in start_game[i]:
        print(num, end=' ')
    # if i != len(start_game) - 1:
    print()


def get_result(start_game):
    if start_game[0][0] == start_game[0][1] == start_game[0][2] == 1:
        return 1
    if start_game[1][0] == start_game[1][1] == start_game[1][2] == 1:
        return 1
    if start_game[2][0] == start_game[2][1] == start_game[2][2] == 1:
        return 1
    if start_game[0][0] == start_game[1][0] == start_game[2][0] == 1:
        return 1
    if start_game[0][1] == start_game[1][1] == start_game[2][1] == 1:
        return 1
    if start_game[0][2] == start_game[1][2] == start_game[2][2] == 1:
        return 1
    if start_game[0][0] == start_game[1][1] == start_game[2][2] == 1:
        return 1
    if start_game[0][2] == start_game[1][1] == start_game[2][0] == 1:
        return 1
    if start_game[0][0] == start_game[0][1] == start_game[0][2] == 2:
        return 2
    if start_game[1][0] == start_game[1][1] == start_game[1][2] == 2:
        return 2
    if start_game[2][0] == start_game[2][1] == start_game[2][2] == 2:
        return 2
    if start_game[0][0] == start_game[1][0] == start_game[2][0] == 2:
        return 2
    if start_game[0][1] == start_game[1][1] == start_game[2][1] == 2:
        return 2
    if start_game[0][2] == start_game[1][2] == start_game[2][2] == 2:
        return 2
    if start_game[0][0] == start_game[1][1] == start_game[2][2] == 2:
        return 2
    if start_game[0][2] == start_game[1][1] == start_game[2][0] == 2:
        return 2
    count = 0
    for row in start_game:
        for num in row:
            if num == 1 or num == 2:
                count += 1
    if count == 9:
        return 3
    else:
        return 4


result = get_result(start_game)
print(result)


def get_0_index(start_game):
    index_0_list = list()
    if start_game[0][0] == 0:
        index_0_list.append(1)
    if start_game[0][1] == 0:
        index_0_list.append(2)
    if start_game[0][2] == 0:
        index_0_list.append(3)
    if start_game[1][0] == 0:
        index_0_list.append(4)
    if start_game[1][1] == 0:
        index_0_list.append(5)
    if start_game[1][2] == 0:
        index_0_list.append(6)
    if start_game[2][0] == 0:
        index_0_list.append(7)
    if start_game[2][1] == 0:
        index_0_list.append(8)
    if start_game[2][2] == 0:
        index_0_list.append(9)
    return index_0_list


if result == 4:
    index_0_list = get_0_index(start_game)
    # computer win
    for num in index_0_list:
        temp_game = copy.deepcopy(start_game)
        temp_game = into_game(num, temp_game, 2)
        if get_result(temp_game) == 2:
            print(num)
    # player not win
    for num in index_0_list:
        temp_game = copy.deepcopy(start_game)
        temp_game = into_game(num, temp_game, 1)
        if get_result(temp_game) == 1:
            print(num)
