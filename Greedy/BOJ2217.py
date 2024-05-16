import sys

# 로프 개수, 로프의 최대중량 입력
n = int(input())
rope = [ int(sys.stdin.readline()) for _ in range(n)]
rope = sorted(rope, reverse=True)

result = [ rope[i] * (i+1) for i in range(n) ]
print(max(result))
