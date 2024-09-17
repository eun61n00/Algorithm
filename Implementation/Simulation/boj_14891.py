# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14891 톱니바퀴

from collections import deque


def rotate(gears, n, d):
    if d == 1:  # 시계 방향
        gears[n] = [gears[n][-1]] + gears[n][:-1]
    else:  # 반시계 방향
        gears[n] = gears[n][1:] + [gears[n][0]]


def check(gears, n, d):
    if n == 1:
        if gears[1][2] != gears[2][-2] and rotated[2] == False:
            returned.append((2, -d))
            rotated[2] = True
    elif n == 4:
        if gears[3][2] != gears[4][-2] and rotated[3] == False:
            returned.append((3, -d))
            rotated[3] = True
    else:
        if gears[n - 1][2] != gears[n][-2] and rotated[n - 1] == False:
            returned.append((n - 1, -d))
            rotated[n - 1] = True
        if gears[n][2] != gears[n + 1][-2] and rotated[n + 1] == False:
            returned.append((n + 1, -d))
            rotated[n + 1] = True


gears = [[int(char) for char in input()] for _ in range(4)]
gears.insert(0, [])

rotate_num = int(input())
rotate_info = [tuple(map(int, input().split())) for _ in range(rotate_num)]
returned = deque([])

for info in rotate_info:
    rotated = [False] * 5
    rotation = deque([])
    rotation.append(info)
    gear_num, direction = info
    rotated[gear_num] = True
    check(gears, gear_num, direction)  # 주어진 정보 체크
    while returned:
        gear_num, direction = returned.popleft()
        rotation.append((gear_num, direction))
        check(gears, gear_num, direction)

    # 돌리기 (gears 정보 바꾸기)
    for r in rotation:
        n, d = r
        rotate(gears, n, d)


score = 0
for idx, gear in enumerate(gears[1:]):
    if gear[0] == 1:
        score += (2 ** (idx))

print(score)
