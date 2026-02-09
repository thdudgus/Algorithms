import sys
n = int(sys.stdin.readline())
n_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_cards = list(map(int, sys.stdin.readline().split()))
n_cards.sort()

def bi_search(start, end, target, cards):
    while start <= end:
        mid = (start + end) // 2
        if target == cards[mid]:
            return 1
        elif target > cards[mid]:
            start = mid + 1
        else: 
            end = mid - 1
    return 0

# n에 m이 있는지 탐색, target이 m
for m_card in m_cards: 
    print(bi_search(0, len(n_cards)-1, m_card, n_cards), end=' ')
    