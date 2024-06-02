# 문자열을 입력받고 문자열을 순회하면서 만약 O면 점수를 +1 하고 step도 +1, 만약 X를 만나면 step은 다시 1이 된다.
# 문자열에 대한 점수를 출력받고 다음 문자열에 대해 처리

n = int(input())

for i in range(n):
    score = 0
    step = 1
    S = input()
    for j in range(len(S)):
        if S[j] == 'O':
            score += step
            step += 1
        else:
            step = 1
    print(score)