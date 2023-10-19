from collections import deque
from copy import deepcopy

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def bfs(maps, start, goal):
    r, c = start
    queue = deque([(r, c)])
    maps[r][c] = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny > len(maps) - 1 or nx > len(maps[0]) - 1:
                continue

            if maps[ny][nx] == goal:
                return maps[y][x] + 1, ny, nx

            elif maps[ny][nx] == "O" or maps[ny][nx] == "E" or maps[ny][nx] == "S":
                maps[ny][nx] = maps[y][x] + 1
                queue.append((ny, nx))


def solution(maps):
    answer = 0
    maps = [list(row) for row in maps]
    for i in range(len(maps)):
        if "S" in maps[i]:
            start = (i, maps[i].index("S"))
    maps_copy = deepcopy(maps)
    lever = bfs(maps_copy, start, 'L')
    if not lever:
        return -1
    end = bfs(maps, (lever[1], lever[2]), 'E')
    if not end:
        return -1
    else:
        return lever[0] + end[0]
