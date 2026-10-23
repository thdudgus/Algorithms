def solution(dartResult):
    score = []
    num = 0
    
    for d in dartResult:
        if d.isdigit():
            num = num*10 + int(d)
        elif d == 'S':
            score.append(num**1)
            num = 0
        elif d == 'D':
            score.append(num**2)
            num = 0
        elif d == 'T':
            score.append(num**3)
            num = 0
        elif d == '#':
            score[-1] *= -1
        elif d == '*':
            score[-1] *= 2
            if len(score) >= 2:
                score[-2] *= 2
    return sum(score)