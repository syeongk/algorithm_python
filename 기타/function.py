"""
def 함수명(매개변수):
    소스코드
    return 반환값              # 함수 안에서 결과까지 출력하는 경우 return문 없이 작성
"""

def add(a,b):
    return a+b

print(add(3,7))


def add(a,b):
    print('함수의 결과: ', a+b)

add(3,7)


a = 0                         # 함수 안에서 함수 밖의 변수 데이터를 변경하고자 할 때, 함수에서 global 키워드로 변수 지정
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)


"""
람다식
1. 간단한 함수를 정의할 때
2. map과 함께 간단한 변환작업
3. 파이썬의 정렬 라이브러리를 사용 시, 정렬 기준(Key)을 설정할 때

lambda 매개변수 : 식
"""

#1
print((lambda a,b: a+b)(3,7))

#2
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

#3
array = sorted(array, key=lambda student: student[1])
