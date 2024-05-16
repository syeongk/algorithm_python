# O(nlogn)
import sys

# 학생의 수 입력
n = int(sys.stdin.readline())

# N명의 학생 정보를 입력받아 리스트에 저장
arr = []
for i in range(n):
    # 튜플 생성
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    # arr에 튜플을 append 한다.
    arr.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여 점수를 기준으로 정렬
arr = sorted(arr, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in arr:
    print(student[0], end=' ')