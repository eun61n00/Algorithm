# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 이것이 코딩 테스트다 Ch5 #3 음료수 얼려 먹기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    graph[x][y] = 1 # 방문 처리

    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 맵을 벗어나면 continue
        if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
            continue

        if graph[nx][ny] == 0:
            dfs(nx, ny)

result = 0
for i in range(n):
    for j in range(m):
        # 뚫려 있으면 음료수 한 칸이라도 부을 수 있음
        if graph[i][j] == 0:
            dfs(i, j)
            result += 1

print(result)