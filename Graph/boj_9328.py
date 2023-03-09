# usr/bin/env python
# -*- coding: utf8 -*-
# boj 9328 열쇠

# *****************
# .............**$*
# *B*A*P*C**X*Y*.X.
# *y*x*a*p**$*$**$*
# *****************
# cz(이미 가지고 있는 열쇠)

# 1
# 5 9
# *********
# .......a*
# ***.*****
# *$Ab*****
# *********
# 0

import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def can_visit(val, key_list):
    if val == '.':
        return True
    elif val == '$':
        return True
    elif ord('a') <= ord(val) <= ord('z'):
        return True
    elif ord('A') <= ord(val) <= ord('Z') and val.lower() in key_list:
        return True
    else:
        return False

def bfs(x, y, graph):
    cnt = 0
    queue = deque([(x, y)])
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1:
                continue

            if graph[nx][ny] != '*' and visited[nx][ny] == False:
                if graph[nx][ny] == '.':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == '$':
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = '.'
                    cnt += 1
                elif ord('a') <= ord(graph[nx][ny]) <= ord('z'):
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    key_list.append(graph[nx][ny])
                    graph[nx][ny] = '.'
                elif ord('A') <= ord(graph[nx][ny]) <= ord('Z') and graph[nx][ny].lower() in key_list:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = '.'
                else:
                    continue

    return cnt

test_case = int(input().rstrip())
for _ in range(test_case):
    h, w = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    key_list = list(input().rstrip())
    if key_list == [0]:
        key_list = []

    start_points= []
    for idx, val in enumerate(board[0]):
        if can_visit(val, key_list):
            start_points.append((0, idx))
    for idx, val in enumerate(board[h - 1]):
        if can_visit(val, key_list):
            start_points.append((h - 1, idx))
    for idx in range(h - 1):
        if can_visit(board[idx][0], key_list):
            start_points.append((idx, 0))
        elif can_visit(board[idx][w - 1], key_list):
            start_points.append((idx, w - 1))

    # start_point를 왔다갔다 -> board에 더이상 변화가 없을 때까지
    answer = 0
    while True:
        board_copy = deepcopy(board)
        for x, y in start_points:
            answer += bfs(x, y, board)
        if board == board_copy:
            break
    print(answer)