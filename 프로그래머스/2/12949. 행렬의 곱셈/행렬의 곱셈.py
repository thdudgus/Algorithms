def solution(arr1, arr2):
    rows, cols = len(arr1), len(arr2[0])  # 결과 행렬의 크기
    answer = [[0] * cols for _ in range(rows)]  # 0으로 초기화된 결과 행렬
    for i in range(rows):  # arr1의 행
        for j in range(cols):  # arr2의 열
            for k in range(len(arr2)):  # 내적 연산
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer
