n = int(input())
student = list(map(int, input().split()))
student.sort()
result = []
for i in range(n):
    result.append(student[i]+student[-1-i])
print(min(result))