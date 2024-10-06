def solution(n):
    b = list(bin(n)[2:])
    count = b.count('1')

    while 1:
        n += 1
        b = list(bin(n)[2:])
        if count == b.count('1'):
            break
    answer = n
    return answer