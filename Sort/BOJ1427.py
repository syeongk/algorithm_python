numbers = input()  # 숫자를 문자열로 받기

numbers_sort = [ int(i) for i in numbers ] # 문자열을 숫자형으로 바꾸어주고, 리스트에 저장
numbers_sort = sorted(numbers_sort, reverse=True) # 내림차순 정렬

for i in numbers_sort:
    print(i, end='')