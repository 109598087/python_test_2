import copy


def is_illegal_num(num):
    if not num.isnumeric:
        return True
    else:
        return False


def into_start_game(num, start_game, player_computer):
    if num == 1 and start_game[0][0] == 0:
        start_game[0][0] = player_computer
    elif num == 2 and start_game[0][1] == 0:
        start_game[0][1] = player_computer
    elif num == 3 and start_game[0][2] == 0:
        start_game[0][2] = player_computer
    elif num == 4 and start_game[1][0] == 0:
        start_game[1][0] = player_computer
    elif num == 5 and start_game[1][1] == 0:
        start_game[1][1] = player_computer
    elif num == 6 and start_game[1][2] == 0:
        start_game[1][2] = player_computer
    elif num == 7 and start_game[2][0] == 0:
        start_game[2][0] = player_computer
    elif num == 8 and start_game[2][1] == 0:
        start_game[2][1] = player_computer
    elif num == 9 and start_game[2][2] == 0:
        start_game[2][2] = player_computer
    else:
        print('Error')
    return start_game


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


def print_game(start_game):
    # 2 3 4 ???
    for i in range(len(start_game)):
        for num in start_game[i]:
            print(num, end=' ')
        # if i != len(start_game) - 1:
        print()


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
