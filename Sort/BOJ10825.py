
import sys
n = int(input())
students = [ list(sys.stdin.readline().split()) for i in range(n)]

'''
# 성적을 정수형으로 변환
for i in range(n):
    for j in range(3):
        list[i][j+1] = int(list[i][j+1])
'''

for student in students:
    student[1] = int(student[1])
    student[2] = int(student[2])
    student[3] = int(student[3])


students = sorted(students, key=lambda student: (-student[1], student[2], -student[3], student))

for student in students:
    print(student[0])