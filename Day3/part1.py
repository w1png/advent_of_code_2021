from sys import stdin
data = stdin.readlines()
nums = list()
gamma_rate_bits = sum([int(i) for i in data]) / len(data)
for line in list(map(str.rstrip, data)):
    for i, char in enumerate(line):
        if len(nums) - 1 < i:
            nums.append(0)
        else:
            nums[i] += int(char)
gamma_rate_bits = ''.join(['1' if i > len(data)//2 else '0' for i in nums])
gamma_rate = int(gamma_rate_bits, 2)
epsilon_rate = int(''.join(["1" if i == "0" else "0" for i in gamma_rate_bits]), 2)
print(epsilon_rate * gamma_rate)
