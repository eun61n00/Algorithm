# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 4179 불!

from collections import deque

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().strip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            loc_j = (i, j)
        elif graph[i][j] == 'F':
            loc_f = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(j, f):
    result = 0
    queue_j = deque([j])
    queue_f = deque([f])
    queue_f_tmp = deque()

    while queue_j:
        j_x, j_y = queue_j.popleft()

        for i in range(4):

            j_nx = j_x + dx[i]
            j_ny = j_y + dy[i]

            if j_nx < 0 or j_ny < 0 or j_nx > r - 1 or j_ny > c - 1:
                result += 1
                return result

            if graph[j_nx][j_ny] == '.':
                graph[j_nx][j_ny] = 'J'
                graph[j_x][j_y] = '.'
                queue_j.append((j_nx, j_ny))
                result += 1

        while queue_f:

            f_x, f_y = queue_f.popleft()

            for i in range(4):
                f_nx = f_x + dx[i]
                f_ny = f_y + dy[i]

                if f_nx < 0 or f_ny < 0 or f_nx > r - 1 or f_ny > c - 1:
                    continue

                if graph[f_nx][f_ny] != '#':
                    graph[f_nx][f_ny] = 'F'
                    queue_f_tmp.append((f_nx, f_ny))

        [queue_f.append(i) for i in queue_f_tmp]

    return "IMPOSSIBLE"

print(bfs(loc_j, loc_f))
