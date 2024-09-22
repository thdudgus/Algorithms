def solution(n):
    f = []
    f.append(0)
    f.append(1)
    if n > 1:
        for i in range(n - 1):
            f.append(f[i] + f[i+1])
    return f.pop() % 1234567