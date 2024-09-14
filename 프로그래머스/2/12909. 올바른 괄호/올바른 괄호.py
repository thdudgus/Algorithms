def solution(s):
    parent_list = list(s)
    stack=[]
    for i in range(0, len(parent_list)):
        if parent_list[i]=='(':
            stack.append('(')
        elif parent_list[i]==')':
            if len(stack)!=0:
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
        
    return True