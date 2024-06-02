T = int(input())

for i in range(T):
    n, S = input().split()
    n = int(n)
    for s in S:
        print(s*n, end="")
    print()