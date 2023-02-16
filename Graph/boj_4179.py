# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 4179 불!

from collections import deque

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().strip()))

loc_f = (-1, -1)
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'J':
            graph[i][j] = 0
            loc_j = (i, j)
        elif graph[i][j] == 'F':
            graph[i][j] = 1
            loc_f = (i, j)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(j, f):
    queue_j = deque([j])
    queue_f = deque([f])
    if f == (-1, -1):
        queue_f = None

    while queue_j:
        x_j, y_j = queue_j.popleft()

        # 매 분마다 확산하는 불의 위치를 담을 리스트
        fire_list = []

        for i in range(4):
            nx_j = x_j + dx[i]
            ny_j = y_j + dy[i]

            if nx_j < 0 or ny_j < 0 or nx_j > r - 1 or ny_j > c - 1:
                return graph[x_j][y_j] + 1

            if graph[nx_j][ny_j] == '.':
                graph[nx_j][ny_j] = graph[x_j][y_j] + 1
                queue_j.append((nx_j, ny_j))

        while queue_f:
            x_f, y_f = queue_f.popleft()
            for i in range(4):
                nx_f = x_f + dx[i]
                ny_f = y_f + dy[i]

                if nx_f < 0 or ny_f < 0 or nx_f > r - 1 or ny_f > c - 1:
                    continue
                if graph[nx_f][ny_f] != '#':
                    graph[nx_f][ny_f] = 'F'
                    fire_list.append((nx_f, ny_f))

        queue_f = deque(fire_list)

    return "IMPOSSIBLE"

print(bfs(loc_j, loc_f))
