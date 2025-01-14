import sys
input = sys.stdin.readline

s = [0] * 21  # 1부터 20까지의 집합 표현

m = int(input().strip())  # 명령어 개수 입력

for _ in range(m):
    command = input().strip().split()
    
    if len(command) == 2:
        operation, num = command[0], int(command[1])
    else:
        operation = command[0]

    if operation == "add":
        s[num] = 1
    elif operation == "remove":
        s[num] = 0
    elif operation == "check":
        sys.stdout.write("1\n" if s[num] else "0\n")
    elif operation == "toggle":
        s[num] = 0 if s[num] else 1
    elif operation == "all":
        s = [1] * 21
    elif operation == "empty":
        s = [0] * 21
