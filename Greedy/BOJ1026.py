
S = 0
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B_idx = sorted(range(len(B)), key=lambda i: -B[i])
A_sort = sorted(A)

for i in range(N):
    A[B_idx[i]] = A_sort[i]

for i in range(N):
    S += A[i] * B[i]

print(S)