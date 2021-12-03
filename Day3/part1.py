from sys import stdin
data = stdin.readlines()
nums = list()
gamma_rate_bits = sum([int(i) for i in data]) / len(data)
for line in data:
    line = line.rstrip()
    for i, char in enumerate(line):
        if len(nums) - 1 < i:
            nums.append(0)
        else:
            nums[i] += int(char)
gamma_rate_bits = ''.join(['1' if i > len(data)//2 else '0' for i in nums])
gamma_rate = sum([(int(num) * (2 ** i)) for i, num in enumerate(gamma_rate_bits[::-1])])
epsilon_rate_bits = ''.join(["1" if i == "0" else "0" for i in gamma_rate_bits])
epsilon_rate = sum([(int(num) * (2 ** i)) for i, num in enumerate(epsilon_rate_bits[::-1])])
print(epsilon_rate * gamma_rate)
