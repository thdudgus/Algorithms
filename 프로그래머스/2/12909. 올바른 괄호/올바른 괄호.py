def solution(s):
    p = list(s)
    stack = [0]
    
    for i in range(len(p)):
        if p[0] == ')':
            stack.append(p[i])
            break
        elif p[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            if stack[-1] == ')':
                stack.append(p[i])
        elif p[i] == '(' :
            stack.append(p[i])
            
    if len(stack) == 1:
        answer = True
    else: answer = False
    
    return answer