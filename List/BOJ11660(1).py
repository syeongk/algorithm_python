import sys
input = sys.stdin.readline
n, m = map(int, input().split())            #n=4 배열 크기 m=3 질의 갯수
A = [[0] * (n+1)]                           #원본배열 1차원
D = [[0] * (n+1) for _ in range(n + 1)]     #누적합배열 2차원

#원본배열 받기
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)


#합배열 구하기
for i in range(1, n+1):         #인덱스가 1부터 시작
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j] #2차원 합배열 공식

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)

