# 1+2+3+4+5...더하다가 합이 S보다 커졌을 때 더한값 - S = n이 나오는데, 그 n을 더한 것과 더한 개수에서 빼준다.
# 예를들어 S가 5라면 1+2+3 > S, 6-5 = 1, 2+3 이고 더한 개수는 2이다.

num = 1
ans = 0
S = int(input())
while True:
    ans += num
    if ans > S:
        ans -= ans - S
        num -= 1
        break
    num += 1

print(num)