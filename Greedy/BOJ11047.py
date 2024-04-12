import sys
input=sys.stdin.readline

N, K = map(int, input().split())
cnt = 0
coin = sorted([ int(input()) for _ in range(N)], reverse=True)

for i in range(N):
    if K // coin[i] != 0:
        cnt += K // coin[i]
        K %= coin[i]

print(cnt)