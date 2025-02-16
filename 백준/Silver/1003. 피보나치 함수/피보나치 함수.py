t = int(input())
result = [[1, 0], [0, 1], [1, 1]]
case = []
for _ in range(t):
    case.append(int(input()))
m = max(case)
for i in range(3, m+1):
    result.append([result[i-1][0]+result[i-2][0], result[i-1][1]+result[i-2][1]])

for i in case:
    print(result[i][0], result[i][1])
