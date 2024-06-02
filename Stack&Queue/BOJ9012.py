# no : YES/NO 가 두번 출력 되지 않도록 체크
# 괄호 문자열을 입력받고 '(' 을 만나면 스택에 push, ')'을 만나면 '('를 pop 한다.
# pop을 할 때 스택이 비어있으면 NO 출력 : '('가 없는데 ')'가 먼저 나왔다는 뜻
# 문자열을 모두 확인하고 나서, 스택이 비어있고 NO가 이미 출력되지 않았다면 YES 출력 : NO가 출력되지 않았는데 스택이 비어있다는 것은 괄호쌍이 올바른 것
# 스택이 비어있지 않으면 NO 출력 : ')' 가 나오지 않아 '('가 pop 되지 않음

import sys

n = int(input())

for _ in range(n):
    s = []
    no = 0
    S = sys.stdin.readline().rstrip()
    for p in S:
        if p == '(':
            s.append(p)
        else:
            if not s:
                print('NO')
                no += 1
                break
            s.pop()
    if not s and no != 1:
        print('YES')
    elif s:
        print('NO')