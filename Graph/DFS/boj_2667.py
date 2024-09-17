# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 2667 단지번호 붙이기

n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, cnt):
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        cnt += dfs(x - 1, y, 0)
        cnt += dfs(x + 1, y, 0)
        cnt += dfs(x, y - 1, 0)
        cnt += dfs(x, y + 1, 0)
        return cnt
    else:
        return 0

result = 0
cnt_list = []
cnt = 0
for i in range(n):
    for j in range(n):
        cnt = dfs(i, j, 0)
        if cnt > 0:
            result += 1
            cnt_list.append(cnt)

print(result)
for i in sorted(cnt_list):
    print(i)