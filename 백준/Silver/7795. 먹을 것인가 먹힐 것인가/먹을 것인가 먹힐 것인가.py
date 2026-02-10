import sys
n = int(sys.stdin.readline())

def comparison(start, end, target, bs):
    while start <= end:
        mid = (start + end) // 2
        if bs[mid] < target:
            start = mid + 1
        else: # bs[mid] == target인 경우엔 어차피 개수를 안 세기 때문에 같은 처리
            end = mid - 1
    return start

for _ in range(n):
    count = 0
    a, b = sys.stdin.readline().split()
    a_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes = list(map(int, sys.stdin.readline().split()))
    b_sizes.sort()
    for a_size in a_sizes:
        if a_size > b_sizes[-1]:
            count += len(b_sizes)
        elif a_size <= b_sizes[0]:
            continue
        else: count += comparison(0, len(b_sizes)-1, a_size, b_sizes)
    print(count)
