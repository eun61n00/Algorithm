# usr/bin/env python
# -*- coding: utf8 -*-
# boj 2563 색종이

# 예제입력
# 3
# 3 7
# 15 7
# 5 2

# 예제 출력
# 260

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

max_x = max([x + 10 for x, y in points])
max_y = max([y + 10 for x, y in points])

board = [[0 for _ in range(max_y)] for _ in range(max_x)]

for x, y in points:
    for i in range(10):
        for j in range(10):
            board[x + i - 1][y + j - 1] = 1

answer = 0
for x in range(max_x):
    for y in range(max_y):
        if board[x][y] == 1:
            answer += 1

print(answer)