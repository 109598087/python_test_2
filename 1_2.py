import copy

from common_function import get_0_index, into_start_game, get_result, print_game


def computer_go(start_game):
    index_0_list = get_0_index(start_game)
    # computer win
    for num in index_0_list:
        temp_game = copy.deepcopy(start_game)
        temp_game = into_start_game(num, temp_game, 2)
        if get_result(temp_game) == 2:
            return num
    # stop player win
    for num in index_0_list:
        temp_game = copy.deepcopy(start_game)
        temp_game = into_start_game(num, temp_game, 1)
        if get_result(temp_game) == 1:
            return num
    live_two_position_list = get_live_two_position(start_game)
    if len(live_two_position_list) == 1:
        return live_two_position_list[0]
    # good choice
    good_list = [5, 1, 3, 7, 9]
    for num in good_list:
        if num in index_0_list:
            return num
    # random choice
    for num in index_0_list:
        return num


def get_live_two_position(start_game):
    index_0_list = get_0_index(start_game)
    num_list = list()
    for num in index_0_list:
        temp_game = copy.deepcopy(start_game)
        temp_game = into_start_game(num, temp_game, 1)
        count = 0
        if temp_game[0][0] == temp_game[0][1] == 1 and temp_game[0][2] == 0:
            count += 1
        if temp_game[1][0] == temp_game[1][1] == 1 and temp_game[1][2] == 0:
            count += 1
        if temp_game[2][0] == temp_game[2][1] == 1 and temp_game[2][2] == 0:
            count += 1

        if temp_game[0][0] == temp_game[1][0] == 1 and temp_game[2][0] == 0:
            count += 1
        if temp_game[0][1] == temp_game[1][1] == 1 and temp_game[2][1] == 0:
            count += 1
        if temp_game[0][2] == temp_game[1][2] == 1 and temp_game[2][2] == 0:
            count += 1

        if temp_game[0][0] == temp_game[0][2] == 1 and temp_game[0][1] == 0:
            count += 1
        if temp_game[1][0] == temp_game[1][2] == 1 and temp_game[1][1] == 0:
            count += 1
        if temp_game[2][0] == temp_game[2][2] == 1 and temp_game[2][1] == 0:
            count += 1

        if temp_game[0][0] == temp_game[2][0] == 1 and temp_game[1][0] == 0:
            count += 1
        if temp_game[0][1] == temp_game[2][1] == 1 and temp_game[1][1] == 0:
            count += 1
        if temp_game[0][2] == temp_game[2][2] == 1 and temp_game[1][2] == 0:
            count += 1

        if temp_game[0][2] == temp_game[0][1] == 1 and temp_game[0][0] == 0:
            count += 1
        if temp_game[1][2] == temp_game[1][1] == 1 and temp_game[1][0] == 0:
            count += 1
        if temp_game[2][2] == temp_game[2][1] == 1 and temp_game[2][0] == 0:
            count += 1

        if temp_game[2][0] == temp_game[1][0] == 1 and temp_game[0][0] == 0:
            count += 1
        if temp_game[2][1] == temp_game[1][1] == 1 and temp_game[0][1] == 0:
            count += 1
        if temp_game[2][2] == temp_game[1][2] == 1 and temp_game[0][2] == 0:
            count += 1

        if temp_game[0][0] == temp_game[1][1] == 1 and temp_game[2][2] == 0:
            count += 1
        if temp_game[0][0] == temp_game[2][2] == 1 and temp_game[1][1] == 0:
            count += 1
        if temp_game[2][2] == temp_game[1][1] == 1 and temp_game[0][0] == 0:
            count += 1

        if temp_game[0][2] == temp_game[1][1] == 1 and temp_game[2][0] == 0:
            count += 1
        if temp_game[0][2] == temp_game[2][0] == 1 and temp_game[1][1] == 0:
            count += 1
        if temp_game[2][0] == temp_game[1][1] == 1 and temp_game[0][2] == 0:
            count += 1
        if count == 2:
            num_list.append(num)
    return num_list


M = int(input())
player_num_list = list()
computer_num_list = list()
start_game = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
if M == 1:
    while True:
        start_game = into_start_game(computer_go(start_game), start_game, 2)
        print_game(start_game)
        result = get_result(start_game)
        if result != 4:
            break

        player_go = int(input())
        start_game = into_start_game(player_go, start_game, 1)
        # print_game(start_game)
        result = get_result(start_game)
        if result != 4:
            break
    result = get_result(start_game)
else:
    while True:
        player_go = int(input())
        start_game = into_start_game(player_go, start_game, 1)
        # print_game(start_game)
        result = get_result(start_game)
        if result != 4:
            break
        start_game = into_start_game(computer_go(start_game), start_game, 2)
        print_game(start_game)
        result = get_result(start_game)
        if result != 4:
            break
print(result)

# input
# 1
# 5
# 2
# 4
# 9
# output
# 3

# input
# 1
# 5
# 2
# 4
# 7
# output
# 2

# input
# 2
