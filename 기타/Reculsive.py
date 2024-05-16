## 재귀함수 예시
def recursive_function(i):
    if i==100:
        return
    print(i, '번째 재귀함수에서,', i+1, '번째 재귀함수를 호출')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료')

recursive_function(1)


## 팩토리얼 구현 - for문
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

## 팩토리얼 구현 - 재귀
def factorial_reculsive(n):
    # n이 1 이하인 경우 1을 반환
    if n <= 1:
        return 1
    # n! = n*(n-1)!
    return n * factorial_reculsive(n-1)

print('반복적으로 구현: ', factorial_iterative(5))
print('재귀적으로 구현: ', factorial_reculsive(5))


## 최대공약수 계산 (유클리드 호제법)
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(10,12))