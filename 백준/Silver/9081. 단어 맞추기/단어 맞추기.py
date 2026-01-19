n = int(input())

for k in range(n):
    w_input = input()
    word = list(w_input)
    tmp = ""
    flag = False
    pivot = 0
    for i in range(len(word)-1, 0, -1):
        if word[i-1] < word[i]: # 뒤에서 가장 큰 것 찾기
            tmp = word[i-1]
            pivot = i-1
            flag = True
            break
    if flag: # pivot을 찾았을 때만 수행.
        for i in range(len(word)-1, 0, -1):
            if tmp < word[i]: # swap: pivot 뒤쪽에 더 큰 거 찾아서 바꾸기
                word[pivot], word[i] = word[i], word[pivot]
                break
        # pivot 뒤쪽 reverse
        word[pivot+1:] = word[pivot+1:][::-1] 
    print(''.join(word))
