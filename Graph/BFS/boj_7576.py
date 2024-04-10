# !/usr/bin/env python
# -*- coding: utf-8 -*
# boj 7576 토마토

from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

grown_tomatoes = [(i, j) for j in range(m) for i in range(n) if box[i][j] == 1]
ungrown_tomatoes = [(i, j) for j in range(m)
                    for i in range(n) if box[i][j] == 0]
if len(ungrown_tomatoes) == 0:
    print(0)
    exit(0)

queue = deque(grown_tomatoes)
visited = [[False] * m for _ in range(n)]
for i, j in grown_tomatoes:
    visited[i][j] = True

answer = 0
while queue:
    y, x = queue.popleft()
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        elif visited[ny][nx] == True or box[ny][nx] == -1:
            continue
        else:
            visited[ny][nx] = True
            queue.append((ny, nx))
            box[ny][nx] = box[y][x] + 1
            answer = max(answer, box[ny][nx])

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)

print(answer-1)
