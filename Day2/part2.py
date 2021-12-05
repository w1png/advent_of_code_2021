from sys import stdin
y = 0
x = 0
aim = 0
for command in list(map(str.rstrip ,stdin.readlines())):
    if command.startswith("forward "):
        x += int(command[8:])
        y += aim * int(command[8:])
    elif command.startswith("up "):
        aim -= int(command[3:])
    elif command.startswith("down "):
        aim += int(command[5:])
print(f"Answer: {x * y}")