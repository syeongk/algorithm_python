
def solution(numbers, target):
    idx = sum = 0

    def dfs(sum, idx):
        # 결과 비교는 마지막에 인덱스가 끝까지 갔을 때 합니다
        if idx == len(numbers):
            return 1 if sum == target else 0

        # idx를 한칸 움직여주고 curr에 이번 값을 더하거나 뺍니다
        left = dfs(sum + numbers[idx], idx + 1)
        right = dfs(sum - numbers[idx], idx + 1)
        return left + right

    answer = dfs(sum, idx)
    return answer

solution([5,1],4)

