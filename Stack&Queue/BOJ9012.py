## 시간복잡도 :
## stack을 통해 데이터를 추가하고, 길이가 홀수일 때 NO 짝수일 때 YES
## 괄호를 하나하나의 값으로 분리해서 길이를 세야하기 때문에 스택 사용?

import sys
n = int(sys.stdin.readline())

for i in range(n):
    # 입력 받는 법 ㅠㅠ
    stack = list(sys.stdin.readline().rstrip())
    if len(stack) % 2 == 0:
        print("YES")
    else:
        print("NO")


