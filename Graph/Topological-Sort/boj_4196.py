# usr/bin/env python
# -*- coding: utf8 -*-
# boj 4196 도미노

import sys

input = sys.stdin.readline

test_case = int(input().rstrip())
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 도미노 관계 입력받기
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited = dfs(graph, i, visited)
    return visited

answer = sys.maxsize

# 어떤 도미노부터 넘어뜨릴 것인가
cnt = 0
visited = [False if i > 0 else True for i in range(n + 1)]
while False in visited:
    v = min([idx for idx, val in enumerate(visited) if val == False])
    visited = dfs(graph, v, visited)
    cnt += 1
answer = min(answer, cnt)

print(answer)