# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2206 벽 부수고 이동하기

import sys
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [[[0, 0] for _ in range(m)] for __ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue

            if visited[nx][ny][wall] == 0:
                queue.append((nx, ny, wall))
                visited[nx][ny][wall] = visited[x][y][wall] + 1


        for i in range(4):
            nr = r + dir[i][0]
            nc = c + dir[i][1]
            # 맵 범위 안에 있고, 한 번도 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][wall] == 0:
                # 벽이 아니라면 이동하고, 이전경로 + 1 visited 배열에 저장
                if board[nr][nc] == 0:
                    q.append((nr, nc, wall))
                    visited[nr][nc][wall] = visited[r][c][wall] + 1

                # 벽 1번도 안 부쉈고, 다음 이동할 곳이 벽이라면
                if wall == 0 and board[nr][nc] == 1:
                    # 벽을 부순 상태를 1로 표현
                    q.append((nr, nc, 1))
                    # 벽 부순 상태의 visited[nr][nc][1]에 이전경로 + 1 저장
                    visited[nr][nc][1] = visited[r][c][wall] + 1

    return -1


print(bfs())