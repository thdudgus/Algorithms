n = int(input())
words = [input() for _ in range(n)]

def int_sum(words):
    return sum(int(c) for c in words if c.isdigit())

words.sort(key=lambda x: (len(x), int_sum(x), x))
for w in words:
    print(w)