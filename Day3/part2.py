# Keeping it extremely unoptimized bcuz I wasted like 5 hours on this one smh.
from sys import stdin
data = list(map(str.rstrip, stdin.readlines()))
oxygen_gen_rating = set(data.copy())
current_bit = 0

while len(oxygen_gen_rating) != 1:
    remove_list = set()

    nums = [0, 0]
    for line in oxygen_gen_rating:
        if line[current_bit] == '1':
            nums[1] += 1
        else:
            nums[0] += 1
    for line in oxygen_gen_rating:
        if line[current_bit] != ('1' if nums[1] >= nums[0] else '0'):
            remove_list.add(line)
    current_bit += 1
    oxygen_gen_rating = oxygen_gen_rating.difference(remove_list)

co2_scrubber_rating = set(data.copy())
current_bit = 0
while len(co2_scrubber_rating) != 1:
    remove_list = set()

    nums = [0, 0]
    for line in co2_scrubber_rating:
        if line[current_bit] == '1':
            nums[1] += 1
        else:
            nums[0] += 1
    for line in co2_scrubber_rating:
        if line[current_bit] != ('1' if nums[1] < nums[0] else '0'):
            remove_list.add(line)
    current_bit += 1
    co2_scrubber_rating = co2_scrubber_rating.difference(remove_list)

oxygen_gen_rating_decimal = sum([(int(num) * (2 ** i)) for i, num in enumerate(list(oxygen_gen_rating)[0][::-1])])
co2_scrubber_rating_decimal = sum([(int(num) * (2 ** i)) for i, num in enumerate(list(co2_scrubber_rating)[0][::-1])])
print(oxygen_gen_rating_decimal * co2_scrubber_rating_decimal)