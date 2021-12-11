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
        win_board = board
        break
    for board in boards_list:
        for row in board:
            if num in row:
                row[row.index(num)] = None
            if row == [None, None, None, None, None]:
                win_num = int(num)
                stop = True
    for column in [[board[j][i] for j in range(5)] for i in range(5)]:
        if column == [None, None, None, None, None]:
            win_num = int(num)
            stop = True

summ = 0
for line in win_board:
    while None in line:
        line.remove(None)
    summ += sum(map(int, line))
print(win_num * summ)
