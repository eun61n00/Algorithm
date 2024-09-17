# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 18405 경쟁적 전염

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((i, j))

for sec in range(s):

    # 매 초에 확산된 바이러스 위치 저장할 리스트
    spread = []
    while queue:
        i, j = queue.popleft()

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                continue

            if graph[nx][ny] == 0 or (graph[nx][ny] > graph[i][j] and (nx, ny) in spread):
                spread.append((nx, ny))
                graph[nx][ny] = graph[i][j]

    for l in spread:
        queue.append(l)

print(graph[x - 1][y - 1])