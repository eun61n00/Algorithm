# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2178 미로탐색

from collections import deque

n, m = map(int, input().split())
graph = []
visited = [[False for _ in range(m)] for __ in range(n)]

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v[0]][v[1]] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if graph[nx][ny] == 0:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(graph, (0, 0), visited))