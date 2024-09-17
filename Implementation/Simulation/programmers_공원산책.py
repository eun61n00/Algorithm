# !usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 공원 산책

def solution(park, routes):
    answer = []
    h = len(park)
    w = len(park[0])

    # E, W, S, N
    dict = {"E": 0, "W": 1, "S": 2, "N": 3}
    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    # S의 위치 저장
    for i, row in enumerate(park):
        if "S" in row:
            cx, cy = i, row.index("S")

    # 이동하기
    for route in routes:
        direction, count = route.split(" ")
        dx = x[dict[direction]]
        dy = y[dict[direction]]
        for cnt in range(1, int(count) + 1):
            nx, ny = cx + dx * cnt, cy + dy * cnt
            if (nx < 0 or ny < 0 or nx >= h or ny >= w):    # 맵 범위를 벗어나는지 검사
                break
            elif park[nx][ny] == "X":   # 장애물이 있는지 검사
                break
            if cnt == int(count):
                cx += dx * int(count)
                cy += dy * int(count)
    return [cx, cy]