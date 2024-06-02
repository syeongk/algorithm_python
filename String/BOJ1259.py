# 팰린드롬수
# 슬라이싱 : S[::-1]

import sys
S = -1
while True:
    S = sys.stdin.readline().rstrip()
    if S == '0':
        break
    if S == S[::-1]:
        print('yes')
    else:
        print('no')