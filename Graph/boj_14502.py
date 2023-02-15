# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14502 연구소

from collections import deque
from copy import deepcopy
from itertools import combinations

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

graph_original = deepcopy(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    cnt = 1
    queue = deque([])
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue

            if graph[nx][ny] == 0: # 아직 바이러스가 방문하지 않았다면
                queue.append((nx, ny))
                graph[nx][ny] = 2
                cnt += 1

    return cnt

# 0의 위치를 모두 저장
zeroes = []
virus = []
walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zeroes.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))
        else:
            walls.append((i, j))

wall_added = list(combinations(zeroes, 3))

result = []
for wall in wall_added:
    tmp = deepcopy(graph_original)

    # 벽 세우기
    graph[wall[0][0]][wall[0][1]] = 1
    graph[wall[1][0]][wall[1][1]] = 1
    graph[wall[2][0]][wall[2][1]] = 1

    cnt = 0
    for x, y in virus:
        # 2로 바뀐 횟수 더하기
        cnt += bfs(graph, x, y)

    graph = tmp
    result.append(cnt)

print((n * m) - min(result) - len(walls) - 3)