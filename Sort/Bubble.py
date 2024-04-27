import sys

n = int(input())
my_list = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n-1):
    for j in range(n-1-i):
        if my_list[j] > my_list[j+1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp

for i in range(n):
    print(my_list[i])



