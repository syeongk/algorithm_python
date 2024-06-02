# 카드의 개수 입력, 카드 합 최대값 입력

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards = sorted(cards, reverse=True)
c_sum = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k] <= m :
                c_sum.append(cards[i]+cards[j]+cards[k])

print(max(c_sum))