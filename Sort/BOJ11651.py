import sys

# 좌표 개수 입력 받기
n = int(input())

# [ [0,4], [1,2], [1,-1], [2,2], [3,3] ] 2차원 리스트가 되도록 입력받기
points = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# y좌표 오름차순으로, y좌표가 같다면 x좌표 오름차순으로 저장하기
points = sorted(points, key=lambda point: (point[1],point[0]))

for point in points:
    print(point[0], point[1])