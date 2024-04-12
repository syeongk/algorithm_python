import sys
input = sys.stdin.readline
n,m = map(int, input().split())
A = [0] + list(map(int, input().split()))
S = [0] * (n+1)

#1차원 누적합배열 구현
for i in range(1, n+1):
    S[i] = S[i-1] + A[i]

#1차원 부분합배열 구현
for _ in range(m):          #반복문에서 질의 입력받기.
    i, j = map(int, input().split())
    result = S[j] - S[i-1]
    print(result)