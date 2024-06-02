from itertools import combinations


n, m = map(int, input().split())
cards = list(map(int, input().split()))

combi = list(combinations(cards,3))
result = []

for i in range(len(combi)):
    if sum(combi[i]) <= m:
        result.append(sum(combi[i]))

print(max(result))