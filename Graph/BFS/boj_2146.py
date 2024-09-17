# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2146 다리 만들기

import sys
input = sys.stdin.readline
n = int(input().rstrip())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


# bfs 진행하며 다른 섬 만나면(1 만나면) 반복문 중단
def bfs(graph, s):
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))
    x, y = s
    for dx, dy in move:
        nx, ny = x + dx, y + dy

