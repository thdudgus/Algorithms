def solution(s):
    stack = []  # 비어 있는 스택 생성
    for char in s:  # 문자열 s의 각 문자를 순서대로 확인
        if stack and stack[-1] == char:  # 스택이 비어있지 않고, 스택 맨 위 문자와 현재 문자가 같으면
            stack.pop()  # 스택에서 맨 위 문자 제거 (쌍 제거)
        else:
            stack.append(char)  # 그렇지 않으면 현재 문자를 스택에 추가
    return 1 if not stack else 0  # 스택이 비어 있으면 1, 아니면 0 반환
