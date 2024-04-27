## 선택정렬 : 가장 작은 원소를 찾아서 (정렬되지 않은 부분)맨 앞으로 이동

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):  # 정렬할 지점
    min_index = i  # 가장 작은 원소의 인덱스 시작점 (계속 비교하며 바뀜)
    for j in range(i+1, len(array)):  # 비교하고자 하는 인덱스
        if array[min_index] > array[j]:  # min_index의 값이 더 클 때 작은 원소로 값 변경
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 모든 원소에 접근하여 가장 작은 원소의 인덱스를 알아내고
                                                             # 가장 작은 원소와 정렬할 지점의 원소를 스와프함

print(array)