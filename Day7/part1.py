from sys import stdin

data = list(map(int, stdin.readlines()[0].split(',')))
print(len(data))
min = 0
for i in set(data):
    total = 0
    for j in data:
        total += abs(i - j)
    if min == 0 or total < min:
        min = total
        
print("Answer: ", min)

