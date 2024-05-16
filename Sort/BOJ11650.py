# 시간복잡도 : O(nlogn)

import sys

# 점의 개수 입력
N = int(sys.stdin.readline())

# 점을 리스트 내부에 있는 튜플로 입력
points = [tuple(map(int, input().split())) for _ in range(N) ]

sorted_points = sorted(points, key=lambda point: (point[0], point[1]))

for point in sorted_points:
    print(point[0], point[1])