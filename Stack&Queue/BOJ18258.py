import sys
from collections import deque

# 명령 입력 개수
n = int(input())
queue = deque()


for i in range(n):
    order = sys.stdin.readline().split()

    # Push
    if order[0] == 'push':
        queue.append(int(order[1]))

    # Pop
    elif order[0] == 'pop':

        # 큐에 값이 없을 때
        if len(queue) == 0:
            print(-1)

        # 값이 있을 때 front 값 Pop
        else:
            print(queue.popleft())

    # Size
    elif order[0] == 'size':
        print(len(queue))

    # Empty
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    # Front
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    # Back
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
