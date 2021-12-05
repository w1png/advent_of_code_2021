from sys import stdin
measurements = list(map(int, stdin.readlines()))
prev = measurements[0]
answer = 0
for depth in measurements:
    answer += 1 if depth > prev else 0
    prev = depth
print(f"Answer: {answer}")
# 1602