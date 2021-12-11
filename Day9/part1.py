# works with the test input 
from sys import stdin

data = [list(map(int, line)) for line in list(map(list, map(str.rstrip, stdin.readlines())))]

low_points = list()
for i, row in enumerate(data):
    for j, num in enumerate(row):
        if min(num, data[i + (1 if i + 1 <= len(data) - 1 else 0)][j], data[i - (1 if i - 1 >= 0 else 0)][j], row[j - (1 if j - 1 >= 0 else 0)], row[j + (1 if j + 1 <= len(row) - 1 else 0)]) == num:
            low_points.append(num)

print(sum(low_points) + len(low_points))