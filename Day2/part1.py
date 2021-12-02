from sys import stdin

y = 0
x = 0
for command in stdin.readlines():
    command = command.rstrip()
    if command.startswith("forward "):
        x += int(command[8:])
    elif command.startswith("up "):
        y -= int(command[3:])
    elif command.startswith("down "):
        y += int(command[5:])

print(f"Answer: {x * y}")