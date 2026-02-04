import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]
num.sort()
sys.stdout.write('\n'.join(map(str, num)))