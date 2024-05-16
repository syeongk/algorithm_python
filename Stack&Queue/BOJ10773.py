## 시간복잡도 : O(nlogn)
## 수를 저장하는데 가장 최근의 숫자를 없애야 하므로 스택 자료구조 사용

import sys
# 숫자의 갯수 입력
n = int(sys.stdin.readline())
# 스택(리스트) 생성
stack = []

for i in range(n):
    # 숫자 입력받기, 합을 구해야 하므로 정수형 변환
    num = int(sys.stdin.readline())
    # 0일 때 pop
    if num==0:
        stack.pop()
    # 0보다 큰 수일 때 push
    else:
        stack.append(num)

print(sum(stack))