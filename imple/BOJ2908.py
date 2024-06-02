# a[::-1] 은 문자열만 가능하다.

a,b = input().split()
li = []
li.append(a[::-1])
li.append(b[::-1])

print(max(li))

