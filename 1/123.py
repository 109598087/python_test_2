import copy


def getPlayer(p):
    if p % 2 == 0:
        return "2"
    else:
        return "1"


def record(player, nine_square_division, times):
    position = "0"
    new_nine_square_division = copy.deepcopy(nine_square_division)
    if player == 2:
        position = str(get_next_step(nine_square_division, times))
        print("Computer:" + position)
    elif player == 1:
        while 1:
            position = input("Player:")
            if position.isdigit():
                break
            else:
                print("Error")
    if int(position) >= 1 and int(position) <= 9:
        if new_nine_square_division[int(position) - 1] == "0":
            new_nine_square_division[int(position) - 1] = getPlayer(player)
            times += 1
            player = int(getPlayer(player + 1))
            return new_nine_square_division, player, times
    print("Error")
    return record(player, nine_square_division, times)


def print_nine_square_division(nine_square_division):
    print(nine_square_division[:3])
    print(nine_square_division[3:6])
    print(nine_square_division[6:])


def get_single_result(nine_square_division, times):
    if times < 9:
        win = "4"
    else:
        win = "3"
    for i in range(3):
        if nine_square_division[0 + i * 3] != "0" and nine_square_division[0 + i * 3] == nine_square_division[
            1 + i * 3] and nine_square_division[1 + i * 3] == nine_square_division[2 + i * 3]:
            return nine_square_division[0 + i * 3]
        if nine_square_division[0 + i] != "0" and nine_square_division[0 + i] == nine_square_division[3 + i] and \
                nine_square_division[3 + i] == nine_square_division[6 + i]:
            return nine_square_division[0 + i]
    if nine_square_division[0] != "0" and nine_square_division[0] == nine_square_division[4] and nine_square_division[
        4] == nine_square_division[8]:
        return nine_square_division[0]
    if nine_square_division[2] != "0" and nine_square_division[2] == nine_square_division[4] and nine_square_division[
        4] == nine_square_division[6]:
        return nine_square_division[2]
    return win


def get_win_or_block_step(nine_square_division, times, player):
    new_nine_square_division = copy.deepcopy(nine_square_division)
    p = 0
    while p < len(new_nine_square_division):
        if new_nine_square_division[p] == "0":
            new_nine_square_division[p] = player
            test_result = get_single_result(new_nine_square_division, times + 1)
            if test_result == player: return p + 1
            new_nine_square_division = copy.deepcopy(nine_square_division)
        p += 1
    if player == "2": return get_win_or_block_step(nine_square_division, times, "1")  # 阻擋
    return 0


def check_step(position, player):
    return position == player or position == "0"


def get_double_lines_step(nine_square_division, times, player):
    p = 0
    if nine_square_division[4] == player:
        if (nine_square_division[2] == player or nine_square_division[6] == player) and nine_square_division[0] == "0":
            return 1
        if (nine_square_division[0] == player or nine_square_division[8] == player) and nine_square_division[2] == "0":
            return 3
        if (nine_square_division[0] == player or nine_square_division[8] == player) and nine_square_division[6] == "0":
            return 7
        if (nine_square_division[2] == player or nine_square_division[6] == player) and nine_square_division[8] == "0":
            return 9
    test_nine_square_division = copy.deepcopy(nine_square_division)
    for i in range(9):
        if test_nine_square_division[i] == "0":
            test_nine_square_division[i] = player
            enemy = getPlayer(int(player) + 1)
            if get_win_or_block_step(test_nine_square_division, times + 1, enemy) != 0: return i + 1
    if player == "1": return get_double_lines_step(nine_square_division, times, "2")  # 阻擋兩條可能路徑
    return p


def get_next_step(nine_square_division, times):
    if times == 0:  return 5  # 先手搶中
    if times == 1:  # 後手第一步，斜角
        if nine_square_division[4] == "0":
            return 5
        if nine_square_division[0] == "1":
            return 9
        if nine_square_division[2] == "1":
            return 7
        if nine_square_division[6] == "1":
            return 3
        if nine_square_division[8] == "1":
            return 1
    if times == 2:  # 對手隔壁或斜角
        if (nine_square_division[1] == "1" or nine_square_division[3] == "1") and nine_square_division[0] == "0":
            return 1
        if (nine_square_division[5] == "1" or nine_square_division[7] == "1") and nine_square_division[8] == "0":
            return 9
        if nine_square_division[0] == "1" and nine_square_division[8] == "0":
            return 9
        if nine_square_division[2] == "1" and nine_square_division[6] == "0":
            return 7
        if nine_square_division[6] == "1" and nine_square_division[2] == "0":
            return 3
        if nine_square_division[8] == "1" and nine_square_division[0] == "0":
            return 1
        if nine_square_division[4] == "0":
            return 5
        if nine_square_division[0] == "1":
            return 9
        if nine_square_division[2] == "1":
            return 7
        if nine_square_division[6] == "1":
            return 3
        if nine_square_division[8] == "1":
            return 1
    if times == 9:  return
    if times == 8:  # 剩下一步
        for i in range(len(nine_square_division)):
            if nine_square_division[i] == "0": return i + 1
    next_step = get_win_or_block_step(nine_square_division, times, "2")  # 連線
    if next_step != 0: return next_step
    next_step = get_double_lines_step(nine_square_division, times, "1")  # 連線或阻擋兩條可能路徑
    if next_step == 0:  # 隨便下
        p = 0
        while p < len(nine_square_division):
            if nine_square_division[p] == "0": return p + 1
            p += 1
    else:
        return next_step


def main():
    times = 0
    nine_square_division = ["0"] * 9
    player = input("請輸入玩家1或電腦2誰先下(輸入1或2)：")
    while player != "1" and player != "2": player = input("請輸入玩家1或電腦2誰先下(輸入1或2)：")
    player = int(player)
    while times >= 0 and times <= 9:
        nine_square_division, player, times = record(player, nine_square_division, times)
        print_nine_square_division(nine_square_division)
        result = get_single_result(nine_square_division, times)
        if result == "1":
            print("Player win")
            break
        elif result == "2":
            print("Computer win")
            break
        elif result == "3":
            print("Tie")
            break


main()