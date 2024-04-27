array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): # 첫 데이터는 정렬되어 있다고 판단하기 때문에, 두 번째 데이터부터 정렬
    for j in range(i,0,-1): # 정렬할 데이터 j 비교할 데이터 j-1, 정렬할 데이터 1까지 비교할 데이터 0
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)