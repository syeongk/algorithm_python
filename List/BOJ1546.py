n = int(input())
score = list(map(int, input().split()))
new_score = [ 0 for _ in range(n)]      # 리스트 초기화 하지 않으면 오류 발생

max_score = max(score)
# 새로운 성적
for i in range(n):
    new_score[i] = score[i]/max_score * 100

# 새로운 평균
sum = sum(new_score)
new_average = sum

print(new_average)
