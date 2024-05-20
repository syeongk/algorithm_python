# users 리스트에 나이(정수형), 이름(문자열) 저장, 나이 오름차순 정렬
import sys

n = int(input())
users = [ list(sys.stdin.readline().split()) for _ in range(n)]

for i in range(n):
    users[i][0] = int(users[i][0])

users = sorted(users, key=lambda user : user[0])

for user in users:
    print(user[0],user[1])