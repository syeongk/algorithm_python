
import sys
import time

start = time.time()

n = int(input())
my_list = [int(sys.stdin.readline()) for _ in range(n)]

my_list = sorted(my_list)

for i in range (n):
    print(my_list[i])
print('시간 :', time.time()-start)


"""
import sys

n = int(input())
my_list = [int(sys.stdin.readline()) for _ in range(n)]
count = [0] * (max(my_list) + 1)

for i in range(len(my_list)):
    count[my_list[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
"""

import sys
import time
start = time.time()
n = int(sys.stdin.readline())

count = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
print('시간 :', time.time()-start)
