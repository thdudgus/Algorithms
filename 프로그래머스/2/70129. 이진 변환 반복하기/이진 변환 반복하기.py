def solution(s):
    zeros = 0
    trans = 0
    while len(s) != 1 and len(s) > 1:
        trans += 1
        zeros += s.count("0")
        bin_str = s.replace("0", "")  # 모든 '0' 제거
        size = len(bin_str)           # 남은 문자열의 길이 계산
        s = bin(size)[2:]         # 길이를 이진수로 변환하고 '0b' 접두어 제거
    return [trans, zeros]