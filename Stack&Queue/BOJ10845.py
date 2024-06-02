# 입력 많이 받을 때 sys 사용

from collections import deque
import sys

n = int(input())
queue = deque()

for i in range(n):
    li = list(sys.stdin.readline().split())

    if li[0] == 'push':
        queue.append(int(li[1]))
        continue

    elif li[0] == 'pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
        continue

    elif li[0] == 'size':
        print(len(queue))
        continue

    elif li[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
        continue

    elif li[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
        continue

    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
        continue

