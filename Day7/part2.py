from sys import stdin

data = list(map(int, stdin.readlines()[0].split(',')))
min = 0
for i in set(data):
    total = sum([sum([i for i in range(1, abs(i - j) + 1)]) for j in data])
    if min == 0 or total < min:
        min = total

print("Answer:", min)
