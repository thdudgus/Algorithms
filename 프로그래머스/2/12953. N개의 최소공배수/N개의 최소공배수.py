import math
from functools import reduce

# 두 수의 최소공배수 (LCM) 계산 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

# 리스트의 모든 원소의 최소공배수 구하기
def solution(arr):
    return reduce(lcm, arr)
