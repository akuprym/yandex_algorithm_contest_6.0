import sys
import math

n = int(sys.stdin.readline())
line = sys.stdin.readline().split(' ')

array = []

for i in range(0, len(line)):
    if (i < n):
        array.append(int(line[i]))

def find_prefix_sum(nums):
    prefixes = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixes[i] = prefixes[i - 1] + nums[i - 1]
    return prefixes[1:]

prefix_sum = find_prefix_sum(array)

print(' '.join(str(el) for el in prefix_sum))