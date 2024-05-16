import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):

    # 명령 입력받기, input().split() 시간초과 발생
    order = sys.stdin.readline().split()

    # push 명령
    if order[0] == 'push':
        stack.append(int(order[1]))

    # pop 명령
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            popnum = stack[-1]
            stack.pop()
            print(popnum)

    # size 명령
    elif order[0] == 'size':
        print(len(stack))

    # empty 명령
    elif order[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    # top 명령
    else:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

