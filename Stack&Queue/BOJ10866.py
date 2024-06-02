# front : appendleft, popleft
# rear : append, pop
# 특정위치 삽입 : insert, pop


import sys
from collections import deque

n = int(input())
d = deque()

for i in range(n):
    o = list(sys.stdin.readline().split())

    if o[0] == 'push_front':
        d.appendleft(o[1])
        continue

    elif o[0] == 'push_back':
        d.append(o[1])
        continue

    elif o[0] == 'pop_front':
        if len(d)==0:
            print(-1)
        else:
            print(d.popleft())
        continue

    elif o[0] == 'pop_back':
        if len(d)==0:
            print(-1)
        else:
            print(d.pop())
        continue

    elif o[0] == 'size':
        print(len(d))
        continue

    elif o[0] == 'empty':
        if len(d)==0:
            print(1)
        else:
            print(0)
        continue

    elif o[0] == 'front':
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
        continue

    else:
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])
        continue