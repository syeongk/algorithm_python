board = list(input())
#print(len(board))
X_count = 0
D_count = 0

for i in range(len(board)):
    if board[i] == 'X':
        X_count += 1
    else:
        D_count += 1

    if board[i] == '.' and board[i+1] == 'X' or i == len(board)-1 :
        if X_count % 2 == 1:
            print(-1)
            break
        elif X_count % 4 == 0:
            for j in range(X_count):
                board[(i+1) - (D_count+ X_count) + j] = 'A'
            X_count = 0
            D_count = 0
        #elif X_count % 4 == 2:
        #   for j in X_count:


for poli in board:
    print(poli, end="")
#elif X_count % 4 == 2:

