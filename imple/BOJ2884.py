import math

a, b = map(int, input().split())

if a==0:
    a=24

result = ((a*60)+b)-45

print(math.floor(result/60), end=" ")
print(result%60, end=" ")