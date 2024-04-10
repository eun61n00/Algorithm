# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 17142 연구실3

from collections import deque


def bfs(viruses):
    dy = (-1, 0, 1, 0)
    dx = (0, 1, 0, -1)
    visited = [[False] * N for _ in range(N)]
    lab = [[0] * N for _ in range(N)]
    queue = deque(viruses)
    for virus in viruses:
        y, x = virus
        lab[y][x] = 0
    for wall in walls:
        y, x = wall
        lab[y][x] = 1

    time = 0
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            elif lab[ny][nx] == 1 or lab[ny][nx] == 2 or visited[ny][nx] == True:
                continue
            lab[ny][nx] = lab[y][x] + 1
            queue.append((ny, nx))
            time = max(time, lab[ny][nx])
    print(viruses)
    for i in range(len(lab)):
        print(lab[i])
    print(f"time: {time}")
    print("===============")
    return time


def dfs(comb, depth):
    global lab, answer
    if len(comb) == M:
        answer = min(answer, bfs(lab, comb))
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
