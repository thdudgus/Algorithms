def solution(n):
    count = 0
    arr = []
    arr.append(0)
    for i in range(1, n+1):
        arr.append(i)
        
    for i in range (1, n+1):
        for j in range(0, n//2+1):
            if i+j > n:
                break
            if sum(arr[i:i+j+1]) > n:
                break
            if sum(arr[i:i+j+1])==n:
                count+=1
                break
    answer = count
    return answer