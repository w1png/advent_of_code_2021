from sys import stdin

data = [list(map(int, line)) for line in list(map(list, map(str.rstrip, stdin.readlines())))]

def try_index(i, j):
    try:
        data[i][j] += 1
    except:
        pass

flashes = 0

for _ in range(100):
    for line_index, line in enumerate(data):
        for oct_index, oct in enumerate(line):
            data[line_index][oct_index] += 1
            if oct > 9:
                data[line_index][oct_index] = 0
                flashes += 1
                try_index(line_index, oct_index + 1)
                try_index(line_index, oct_index - 1)
                # data[line_index][oct_index + 1] += 1
                # data[line_index][oct_index - 1] += 1
                
                try_index(line_index + 1, oct_index)
                try_index(line_index + 1, oct_index + 1)
                try_index(line_index + 1, oct_index - 1)
                # data[line_index + 1][oct_index]
                # data[line_index + 1][oct_index + 1]
                # data[line_index + 1][oct_index - 1]

                try_index(line_index - 1, oct_index)
                try_index(line_index - 1, oct_index + 1)
                try_index(line_index - 1, oct_index - 1)
                # data[line_index - 1][oct_index]
                # data[line_index - 1][oct_index + 1]
                # data[line_index - 1][oct_index - 1]
    for line in data:
        print(line)
    print()

print(flashes)
