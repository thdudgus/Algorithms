def solution(number, k):
    n = list(str(number))
    stack = []
    
    for i in range(len(n)):
        while k > 0 and stack and stack[-1] < n[i]:
            stack.pop()
            k -= 1
        stack.append(n[i])

    if k > 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
    return answer