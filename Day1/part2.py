from sys import stdin
measurements = list(map(int, stdin.readlines()))
lastsum = sum([measurements[i] for i in range(3)])
answer = 0
for i in range(len(measurements[:-2])):
    summ = measurements[i] + measurements[i + 1] + measurements[i + 2]
    answer += 1 if lastsum < summ else 0
    lastsum = summ
print(f"Answer: {answer}")