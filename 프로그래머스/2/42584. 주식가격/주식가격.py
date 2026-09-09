def solution(prices):
    answer = []
    for i, price in enumerate(prices):
        count = 0
        for k in range(i+1, len(prices)):
            if price <= prices[k]:
                count += 1
            else: 
                count += 1
                break
        answer.append(count)
    return answer