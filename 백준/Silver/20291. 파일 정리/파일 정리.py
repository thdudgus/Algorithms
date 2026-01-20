import re
n = int(input())
file_ = []
for i in range(n):
    file_.append(input())

p = re.compile(r'[a-z]*.([a-z]*)')
result = {}

for f in file_:
    tmp = p.search(f)
    if tmp.group(1) not in result:
        result[tmp.group(1)] = 1
    else:
        result[tmp.group(1)] += 1

for k, v in sorted(result.items()):
    print(k, v)