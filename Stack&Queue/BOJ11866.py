from collections import deque

n,k = map(int, input().split())

# 1번부터 n번까지 숫자가 들어있는 큐 생성
queue = deque([i for i in range(1,n+1)])
# 결과 리스트
result = []

for _ in range(n):
    for _ in range(k-1):
        number = queue.popleft()
        queue.append(number)
    result.append(queue.popleft())

print('<'+ ', '.join(map(str, result)) +'>')