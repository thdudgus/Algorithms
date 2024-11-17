def solution(k, tangerine):
    # 귤 크기별 개수 세기
    tangerineSize = {}
    for size in tangerine:
        if size not in tangerineSize:
            tangerineSize[size] = 0
        tangerineSize[size] += 1

    # 귤 개수를 내림차순으로 정렬
    sortedSize = sorted(tangerineSize.values(), reverse=True)

    # 필요한 귤의 개수만큼 종류 선택
    temp = 0
    count = 0
    for size in sortedSize:
        temp += size
        count += 1
        if temp >= k:  # 원하는 개수를 채우면 종료
            break

    return count