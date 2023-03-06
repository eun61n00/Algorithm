# usr/bin/env python
# -*- coding: utf8 -*-
# boj 9328 열쇠

# *****************
# .............**$*
# *B*A*P*C**X*Y*.X.
# *y*x*a*p**$*$**$*
# *****************
# cz(이미 가지고 있는 열쇠)

import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input().rstrip())
h, w = map(int, input().split())

board = [list(input().rstrip()) for _ in range(h)]
visited = [[False for _ in range(w)] for _ in range(h)]

key_list = list(input().rstrip())
if key_list == [0]:
    key_list = []

start_points= []
# start point 저장하기
for idx, val in enumerate(board[0]):
    if val != '*':
        start_points.append((0, idx))
for idx, val in enumerate(board[h - 1]):
    if val != '*':
        start_points.append((h - 1, idx))
for idx in range(h - 1):
    if board[idx][0] != '*':
        start_points.append((idx, 0))
    elif board[idx][w - 1] != '*':
        start_points.append((idx, w - 1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph):
    queue = deque((x, y))
    # visited[x][y] = True
    answer = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if graph[nx][ny] != '*':



            if graph[nx][ny] == '.':
                queue.append((nx, ny))
                # visited[nx][ny] = True
            elif graph[nx][ny] == '$':
                queue.append((nx, ny))
                graph[nx][ny] = '.' # 이미 간 것으로 변경
                answer += 1
            elif



# start_point를 왔다갔다 -> board에 더이상 변화가 없을 때까지
while True:
    for x, y in start_points:
