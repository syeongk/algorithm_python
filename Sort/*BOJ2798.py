"""
import sys

n = int(input())
my_list = [int(sys.stdin.readline()) for _ in range(n)]

my_list.sort()

for i in range (n):
    print(my_list[i])
"""

"""
import sys
n = int(input())
my_list = [int(sys.stdin.readline()) for _ in range(n)]
count = [0] * (max(my_list) + 1)

# my_list를 순회하면서 해당하는 숫자가 몇 개 있는지 센다.
for i in range(len(my_list)):
    count[my_list[i]] += 1

# count를 순회하면서 계수정렬 결과를 출력한다.
for i in range(len(count)):
    for j in range(count[i]):
        print(i)
"""

