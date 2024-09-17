# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1941 소문난 칠공주

graph = []
for i in range(5):
    graph.append(list(input()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0
answer_list = []


def dfs(graph, start, visited, depth, stack):
    print(f"dfs({depth, stack})")
    global answer, answer_list
    y, x = start
    stack.append(graph[y][x])
    visited[y][x] = True
    if depth == 7:
        if stack.count("S") >= 4:
            answer += 1
            # answer_list.append([stack])
            # print(answer_list)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        if visited[ny][nx] == False:
            stack.append(graph[ny][nx])
            visited[ny][nx] = True
            dfs(graph, (nx, ny), visited, depth + 1, stack)


for i in range(5):
    for j in range(5):
        if graph[i][j] == "S":
            dfs(graph, (i, j), [[False] * 5 for _ in range(5)], 0, [])
            exit(0)

print(answer)
print(answer_list)
