n = int(input())
count= 0
title = '666'
temp = 665
while True:
    temp +=1
    if str(temp).find(title) != -1:
        count+=1
    if count == n:
        answer = temp
        break
print(answer)