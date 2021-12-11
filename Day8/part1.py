from sys import stdin
print("Answer:", sum([sum([1 if len(num) in [2, 4, 3, 7] else 0 for num in line.split(" | ")[1].split(" ")]) for line in list(map(str.rstrip, stdin.readlines()))]))
