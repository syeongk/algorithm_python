#전역변수 선언
check_list = [0] * 4
my_list = [0] * 4
check_secret = 0

#함수 정의
def my_add(s):          #새로 들어온 문자를 처리하는 함수
    global check_list, my_list, check_secret
    if s == 'A':
        my_list[0] += 1
        if my_list[0] == check_list[0]:
            check_secret += 1
    elif s == 'C' :
        my_list[1] += 1
        if my_list[1] == check_list[1]:
            check_secret += 1
    elif s == 'G' :
        my_list[2] += 1
        if my_list[2]== check_list[2]:
            check_secret += 1
    elif s == 'T' :
        my_list[3] += 1
        if my_list[3] == check_list[3]:
            check_secret +=1

def my_remove(s):       #제거되는 문자를 처리하는 함수
    global check_list, my_list, check_secret
    if s == 'A':
        if my_list[0] == check_list[0]:
            check_secret -= 1
        my_list[0] -= 1
    elif s == 'C':
        if my_list[1] == check_list[1]:
            check_secret -= 1
        my_list[1] -= 1
    elif s == 'G':
        if my_list[2] == check_list[2]:
            check_secret -= 1
        my_list[2] -= 1
    elif s == 'T':
        if my_list[3] == check_list[3]:
            check_secret -= 1
        my_list[3] -= 1

#메인 코드
S, P = map(int, input().split())    # S (문자열 크기) P (슬라이딩 윈도우 크기)
Result = 0
A = list(input())                   # A (문자열 데이터)
check_list = list(map(int, input().split()))

for i in range(4):
    if check_list[i] == 0:
        check_secret += 1

for i in range(P):
    my_add(A[i])

if check_secret == 4:
    Result += 1

for i in range(P, S):
    j = i-P
    my_add(A[i])
    my_remove(A[j])
    if check_secret == 4:
        Result += 1

print(Result)