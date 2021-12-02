from sys import stdin
measurements = stdin.readlines()
lastsum = int(measurements[0]) + int(measurements[1]) + int(measurements[2])
answer = 0
for i in range(len(measurements[:-2])):
    summ = int(measurements[i]) + int(measurements[i + 1]) + int(measurements[i + 2])
    if lastsum < summ:
        text = "(increased)"
        answer += 1
    else:
        text = "(decreased)"
    print(summ, text)
    lastsum = summ

print(f"Answer: {answer}")