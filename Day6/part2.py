# this would work with enough time and computational power :)
from sys import stdin

fish_list = list(map(int, stdin.readlines()[0].split(',')))

value_size = dict()
for i in range(1, 6):
    gen = [i]
    for j in range(256):
        new_gen = list()
        print(j)
        for fish in gen:
            if fish == 0:
                new_gen.append(8)
                new_gen.append(6)
            else:
                new_gen.append(fish - 1)
        gen = new_gen
    value_size[i] = len(gen)

value_appearance = dict()
for num in fish_list:
    if num in value_appearance:
        value_appearance[num] += 1
    else:
        value_appearance[num] = 0

total = 0
for i in range(1, 6):
    total += value_appearance[i] * value_size[i]


print("Answer:", total)