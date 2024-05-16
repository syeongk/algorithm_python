def calculate_sum(numbers):
    # 종료 조건: 빈 리스트인 경우
    if not numbers:
        return 0

    # 리스트의 첫 번째 요소를 합계에 더하고 나머지 요소에 대해 재귀 호출
    return numbers[0] + calculate_sum(numbers[1:])

# 예시 실행
result = calculate_sum([1, 2, 3, 4, 5])
print(result)  # 출력: 15