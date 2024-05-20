# 시간복잡도 : O(nlogn)
import sys

# 단어 개수 입력받기
n = int(input())

# 단어들을 입력받고 중복 원소 제거
words = list(set([ sys.stdin.readline().rstrip() for _ in range(n)]))

# 정렬 조건 : 길이 짧은 -> 사전 순으로
words = sorted(words, key=lambda word : (len(word), word))

for word in words:
    print(word)