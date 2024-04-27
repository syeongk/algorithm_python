import sys

n, k = map(int, input().split())

li = list(map(int, input().split()))
li = sorted(li, reverse=True)

print(li[k-1])