'''
1은 집이 있음, 0은 집이 없음
상하좌우 연결 확인
단지수 출력, 단지의 집의 수 오름차순 정렬 출력

n 입력
nxn graph 정보 입력 - 리스트 컴프리헨션 [ sys.. for i in range(n)]

DFS 구현

def dfs:
범위 벗어나면 종료
if graph[r][c] = 1:
해당 노드의 값을 name으로 바꾸어줌
small_c += 1
상 dfs()
하 dfs()
좌 dfs()
우 dfs()

dfs 호출
for i in range(n):
    for j in range(n):
        //범위를 벗어나거나, 현재 노드 방문했다면 False이고 그 반대라면 True 반환
        if dfs(r,c)==True:
         big_c += 1
         name += 1


'''

import sys

n = int(input())
graph = [ list(map(int, sys.stdin.readline().rstrip()))  for i in range(n)]

def dfs(r,c):
    global count

    # 행과 열의 위치가 맵을 벗어나면 종료합니다. *부등호 주의
    if r<=-1 or r>=n or c<=-1 or c>=n:
        return False

    # 맵을 벗어나있지 않다면, 집이 있는 곳인지 확인합니다.
    if graph[r][c] == 1:
        # 집이 있다면, 단지 이름 (2부터) 지정하고 집의 개수 체크
        graph[r][c] = apart
        count += 1
        # 현재 노드의 상,하,좌,우에 있는 노드를 호출합니다.
        dfs(r-1,c) #상
        dfs(r+1,c) #하
        dfs(r,c-1) #좌
        dfs(r,c+1) #우
        return True
    return False

apart = 2
big_c = 0
small_c = []

for i in range(n):
    for j in range(n):
        count = 0
        # 하나의 단지를 찾았다는 것
        if dfs(i,j)==True:
            # 단지 수 증가시킴
            big_c += 1
            # 다음에 실행할 함수에서 단지 이름 변경시킴
            apart += 1
            # 단지 내 집의 수
            small_c.append(count)


small_c = sorted(small_c)

print(big_c)
for i in range(big_c):
    print(small_c[i])