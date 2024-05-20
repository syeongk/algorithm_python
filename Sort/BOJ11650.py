# 시간복잡도 O(nlogn)
import sys

# 좌표의 개수 입력
n = int(input())

# 좌표를 저장할 2차원 리스트 생성
points = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# x좌표 먼저 오름차순 정렬 -> y좌표 오름차순 정렬
points = sorted(points, key=lambda point : (point[0],point[1]))

for point in points:
    print(point[0],point[1])