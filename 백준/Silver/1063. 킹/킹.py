import sys
king, stone, n = sys.stdin.readline().split()
king = list(king)
stone = list(stone)
n = int(n)
king_location = [ord(king[0]) - 64, int(king[1])]
stone_location = [ord(stone[0]) - 64, int(stone[1])]

def directions(dir):
    if dir == 'R': dir = [1, 0]
    elif dir == 'L': dir = [-1, 0]
    elif dir == 'B': dir = [0, -1]
    elif dir == 'T': dir = [0, 1]
    elif dir == 'RT': dir = [1, 1]
    elif dir == 'LT': dir = [-1, 1]
    elif dir == 'RB': dir = [1, -1]
    elif dir == 'LB': dir = [-1, -1]
    return dir

for _ in range(n):
    dir = sys.stdin.readline().rstrip()
    direction = directions(dir)
    flag = False

    king_location = [x+y for x, y in zip(king_location, direction)]
    if king_location == stone_location:
        stone_location = [x+y for x, y in zip(stone_location, direction)]
        flag = True
    if king_location[0] < 1 or king_location[0] > 8 or king_location[1] < 1 or king_location[1] > 8 or stone_location[0] < 1 or stone_location[0] > 8 or stone_location[1] < 1 or stone_location[1] > 8:
        king_location = [x-y for x, y in zip(king_location, direction)]
        if flag: stone_location = [x-y for x, y in zip(stone_location, direction)]
            
print(chr(king_location[0] + 64) + str(king_location[1]))
print(chr(stone_location[0] + 64) + str(stone_location[1]))