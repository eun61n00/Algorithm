# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1926 그림

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# DFS 풀이 - Runtime Error
# def dfs(v, visited):
#     global graph
#     global tmp
#     x, y = v
#     visited[x][y] = True

#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         if not visited[nx][ny] and graph[nx][ny] == 1:
#             visited[nx][ny] = True
#             graph[nx][ny] = graph[x][y] + 1
#             tmp += 1
#             dfs((nx, ny), visited)


# count = 0
# area = 0

# for i in range(n):
#     for j in range(m):
#         if not visited[i][j] and graph[i][j] == 1:
#             count += 1
#             tmp = 1
#             dfs((i, j), visited)
#             area = max(area, tmp)

# print(count)
# print(area)


# BFS 풀이
def bfs(graph, start):
    area = 1
    global visited
    x, y = start
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1

    return area


max_area = 0
painting_count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            painting_count += 1
            max_area = max(max_area, bfs(graph, (i, j)))

print(painting_count)
print(max_area)
