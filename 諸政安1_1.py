import copy

from 諸政安common_function import is_illegal_num, into_start_game, get_result, get_0_index, print_game


def main():
    row1 = input()
    # try:
    if is_illegal_num(row1.split(' ')[0]) or is_illegal_num(row1.split(' ')[1]):
        print('Error')
    else:
        print('OK')

    M = int(row1.split(' ')[0])
    N = int(row1.split(' ')[1])
    # except:
    # print('Error')

    start_game = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]

    player1_list = list()
    player2_list = list()
    # for i in range(N):
    row2 = input()
    row_split = row2.split(' ')
    # remove error num
    row_split = [num for num in row_split if num.isnumeric() and 1 <= int(num) <= 9]

    for i in range(len(row_split)):
        if i % 2 == 0:
            player1_list.append(int(row_split[i]))
        else:
            player2_list.append(int(row_split[i]))

    # add
    if M == 1:
        for num in player1_list:
            start_game = into_start_game(num, start_game, 1)
        for num in player2_list:
            start_game = into_start_game(num, start_game, 2)
    else:
        for num in player1_list:
            start_game = into_start_game(num, start_game, 2)
        for num in player2_list:
            start_game = into_start_game(num, start_game, 1)

    print_game(start_game)
    result = get_result(start_game)
    print(result)

    if result == 4:
        index_0_list = get_0_index(start_game)
        # computer win
        is_computer_win = False
        for num in index_0_list:
            temp_game = copy.deepcopy(start_game)
            temp_game = into_start_game(num, temp_game, 2)
            if get_result(temp_game) == 2:
                print(num)
                is_computer_win = True
        # player not win
        if is_computer_win == False:
            for num in index_0_list:
                temp_game = copy.deepcopy(start_game)
                temp_game = into_start_game(num, temp_game, 1)
                if get_result(temp_game) == 1:
                    print(num)


main()
