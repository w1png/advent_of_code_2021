from sys import stdin

data = list(map(str.rstrip, stdin.readlines()))

answer = 0
for line in data:
    brackets = {
        "(": 0,
        ")": 0,
        "{": 0,
        "}": 0,
        "<": 0,
        ">": 0,
        "[": 0,
        "]": 0,
    }
    for sym in line:
        brackets[sym] += 1
    if brackets["("] != brackets[")"]:
        answer += 3
        print("()", brackets["("], brackets[")"])
    elif brackets["["] != brackets["]"]:
        answer += 57
        print("[]", brackets["["], brackets["]"])
    elif brackets["<"] != brackets[">"]:
        answer += 25137
        print("<>", brackets["<"], brackets[">"])
    elif brackets["{"] != brackets["}"]:
        answer += 1197
        print("{}", brackets["{"], brackets["}"])
        

print(answer)