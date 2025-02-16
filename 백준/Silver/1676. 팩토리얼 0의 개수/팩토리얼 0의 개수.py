n = int(input())
factorial = 1
for i in range(n):
    factorial *= i+1
count = 0
while factorial % 10 == 0:
    count += 1
    factorial = factorial // 10
print(count)