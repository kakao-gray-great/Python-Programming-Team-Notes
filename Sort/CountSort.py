# 계수 정렬
# 시간 복잡도 O(N + K)
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for arr in array:
    count[arr] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end = ' ')

''' 결과 값
0 0 1 1 2 2 3 4 5 5 6 7 8 9 9 
'''