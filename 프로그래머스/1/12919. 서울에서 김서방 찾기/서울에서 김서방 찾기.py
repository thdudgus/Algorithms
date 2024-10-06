def solution(seoul):
    k=0
    for i in seoul:
        if i == 'Kim':
            return "김서방은 {}에 있다".format(k)
        k+=1