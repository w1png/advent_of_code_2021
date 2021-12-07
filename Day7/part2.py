from sys import stdin

data = list(map(int, stdin.readlines()[0].split(',')))
min = 0
for i in set(data):
    total = 0
    for j in data:
        total += sum([i for i in range(1, abs(i - j) + 1)])
    if min == 0 or total < min:
        min = total

print("Answer: ", min)
