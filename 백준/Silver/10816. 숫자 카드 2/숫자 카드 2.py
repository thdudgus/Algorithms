n = int(input())
nCards = list(map(int, input().split()))
m = int(input())
mCards = list(map(int, input().split()))

count_dict = {}
# nCards에 각 값이 몇 개 있는지 count
for card in nCards:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1

# mCards를 순회하며 개수 출력
result = []
for target in mCards:
    result.append(str(count_dict.get(target, 0))) # 딕셔너리에 있으면 그 값을, 없으면 0을 가져옴

print(" ".join(result))