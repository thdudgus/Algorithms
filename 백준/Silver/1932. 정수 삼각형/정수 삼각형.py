import sys
n = int(sys.stdin.readline())
tri = []
for _ in range(n):
    tri.append(list(map(int, sys.stdin.readline().split())))

for i in range(n-2, -1, -1):
    for j in range(len(tri[i])):
        if i+1 < n and j+1 < len(tri[i+1]):
            tri[i][j] = max(tri[i][j]+tri[i+1][j],tri[i][j]+tri[i+1][j+1])
print(tri[0][0])