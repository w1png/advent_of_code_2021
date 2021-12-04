# Works agains the test input but can't figure out why it doesn't work against the real one.
from sys import stdin

data = list(map(str.rstrip, stdin.readlines()))
while '' in data:
    data.remove('')
draw_order = data[0].split(',')

def get_boards_list():
    return [[[num for num in data[i].split()] for i in range(i, i + 5)] for i in range(1, len(data[1:]), 5)]

boards_list = get_boards_list()
stop = False
for num in draw_order:
    if stop:
        break
    for board in boards_list:
        for line in board:
            if num in line:
                line.remove(num)
            if len(line) == 0:
                win_num = int(num)
                stop = True
        if stop:
            win_board = board
            break

summ = 0
for line in win_board:
    summ += sum(map(int, line))

print("Answer:", summ * win_num)
