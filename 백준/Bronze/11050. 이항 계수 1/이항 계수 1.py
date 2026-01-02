import math
def test(a, b):
    n = math.factorial(a)
    m = math.factorial(a-b)
    k = math.factorial(b)

    return int(n/(m*k))

x, y = map(int, input().split())
result = test(x, y)
print(result)