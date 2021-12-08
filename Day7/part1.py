from sys import stdin

data = list(map(int, stdin.readlines()[0].split(',')))
min = 0

for i in set(data):
    total = sum([abs(i - j) for j in data])
    if min == 0 or total < min:
        min = total
        
print("Answer:", min)
