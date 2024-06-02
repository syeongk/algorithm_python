import sys

nums = [ int(sys.stdin.readline()) for i in range(9) ]

print(min(nums))
print(nums.index(min(nums))+1)