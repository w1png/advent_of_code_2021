from sys import stdin

fish_list = list(map(int, stdin.readlines()[0].split(',')))
for i in range(80):
    new_gen = list()
    for fish in fish_list:
        if fish == 0:
            new_gen.append(8)
            new_gen.append(6)
        else:
            new_gen.append(fish - 1)
    fish_list = new_gen

print("Answer:", len(fish_list))
