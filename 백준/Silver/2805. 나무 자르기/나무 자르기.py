tmp = list(map(int, input().split()))
n = tmp[0]
m = tmp[1]
trees = list(map(int, input().split()))

low = 0
high = max(trees)
result = 0 # m을 만족하는 최대 h

while low <= high:
    mid = (low + high) // 2
    total = sum(tree - mid for tree in trees if tree > mid)
    if total >= m:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)
