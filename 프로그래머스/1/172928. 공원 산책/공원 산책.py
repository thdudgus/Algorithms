def solution(park, routes):
    directions = {
        'N': [-1, 0],
        'S': [1, 0],
        'W': [0, -1],
        'E': [0, 1]
    }

    # 시작 위치 찾기
    for i, p in enumerate(park):
        if 'S' in p:
            row = i
            col = p.index('S')
            break

    h = len(park)
    w = len(park[0])

    for route in routes:
        d, n = route.split()
        n = int(n)

        dr, dc = directions[d]

        # 임시 위치에서 이동 가능 여부 확인
        nr = row
        nc = col
        possible = True

        for _ in range(n):
            nr += dr
            nc += dc

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                possible = False
                break

            if park[nr][nc] == 'X':
                possible = False
                break

        # 모든 이동이 가능할 때만 위치 변경
        if possible:
            row = nr
            col = nc

    return [row, col]