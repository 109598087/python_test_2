import copy

from common_function import get_0_index, into_game, get_result

M = int(input())
player_num_list = list()
computer_num_list = list()
start_game = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]


def computer_go(start_game):
    index_0_list = get_0_index(start_game)
    for num in index_0_list:
        temp_game = copy.deepcopy(start_game)
        temp_game = into_game(num, temp_game, 2)
        if get_result(temp_game) == 2:
            return num


if M == 1:
    start_game = computer_go(start_game)
