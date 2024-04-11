# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 17142 연구실3

from collections import deque


def bfs(selected):
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    visited = [[False] * N for _ in range(N)]

    queue = deque(selected)

    for wall in walls:
        y, x = wall
        lab[y][x] = -1
    for virus in viruses:
        y, x = virus
        lab[y][x] = "*"
        visited[y][x] = True
    for virus in selected:
        y, x = virus
        lab[y][x] = 0

    time = 0
    while queue:
        y, x = queue.popleft()
        # visited[y][x] = True # 방문 처리를 어디서 하냐! 고민해보기
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            elif lab[ny][nx] == -1 or visited[ny][nx] == True:
                continue
            lab[ny][nx] = lab[y][x] + 1
            queue.append((ny, nx))
            visited[ny][nx] = True
            time = max(time, lab[ny][nx])
    # print(selected)
    # for i in range(len(lab)):
    #     print(lab[i])
    # print()
    return time


def dfs(comb, depth):
    global answer, lab, visited
    if len(comb) == M:
        answer = min(answer, bfs(comb))
        return comb
    elif depth == len(viruses):
        return

    comb.append(viruses[depth])
    dfs(comb, depth + 1)

    comb.pop()
    dfs(comb, depth + 1)


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
answer = 50

viruses = [(i, j) for j in range(N) for i in range(N) if lab[i][j] == 2]
walls = [(i, j) for j in range(N) for i in range(N) if lab[i][j] == 1]

dfs(deque(), 0)
print(answer)
