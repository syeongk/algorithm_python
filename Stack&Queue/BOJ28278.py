import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    order = sys.stdin.readline().split()

    # Push 명령
    if order[0] == '1':
        li.append(order[1])

    # Pop 명령, 리스트에 아무것도 없을 때(pop 할 수 없을 때) -1 출력
    elif order[0] == '2':
        if len(li) == 0:
            print(-1)
        else:
            """"
            popnum = li[-1]
            li.pop()
            print(popnum)
            """
            print(li.pop(-1))

    # Size 명령
    elif order[0] == '3':
        print(len(li))

    # Empty 명령, 리스트에 아무것도 없을 때 1 출력
    elif order[0] == '4':
        if len(li)==0:
            print(1)
        else:
            print(0)

    # Top 명령, 리스트에 아무것도 없을 때 -1 출력
    else:
        if len(li)==0:
            print(-1)
        else:
            print(li[-1])
