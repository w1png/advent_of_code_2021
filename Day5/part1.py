from sys import stdin

lines = list(tuple(tuple(map(int, line.split(" -> ")[i].split(","))) for i in [0, 1]) for line in list(map(str.rstrip, stdin.readlines())))
visits = dict()
for line in lines:
    x1, y1 = line[0][0], line[0][1]
    x2, y2 = line[1][0], line[1][1]
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            if (x1, i) in visits:
                visits[(x1, i)] += 1
            else:
                visits[(x1, i)] =  0
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if (i, y1) in visits:
                visits[(i, y1)] += 1
            else:
                visits[(i, y1)] =  0
answer = sum([1 if visits[dot] >= 1 else 0 for dot in visits])

print("Answer:", answer)
                