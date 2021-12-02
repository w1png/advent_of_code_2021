from sys import stdin
measurements = stdin.readlines()
prev = int(measurements[0])
answer = 0
for depth in measurements:
    depth = int(depth)
    if depth > prev:
        answer += 1
    prev = depth
print(f"Answer: {answer}")