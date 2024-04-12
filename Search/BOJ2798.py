import sys

n = int(input())
my_list = [int(sys.stdin.readline()) for _ in range(n)]

my_list.sort()

for i in range (n):
    print(my_list[i])