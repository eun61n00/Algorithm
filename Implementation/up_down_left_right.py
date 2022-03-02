# <이것이 코딩 테스트다>(나동빈, 한빛미디어) 예제 4-1
from sys import stdin

n = int(stdin.readline())
plans = input().split()
x, y = 1, 1
dir_x = [0, 0, -1, 1]
dir_y = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dir_x[i]
            ny = y + dir_y[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)