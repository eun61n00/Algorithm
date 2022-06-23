# boj_1260
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())

def dfs(graph, v, visited, dfs_result):
	visited[v] = True
	dfs_result.append(v)

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited, dfs_result)


def bfs(graph, v, visited):
	queue = deque([start])
	visited[start] = True

	while queue:
		v = queue.popleft()
		bfs_result.append(v)

		for i in graph[v]:
			if not visited[i]:
				queue.append(i)

graph = [[] for _ in range(n + 1)]
for _ in range(n):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False] * (n + 1)
dfs_result = []

visited = [False] * (n + 1)
bfs_result = []

dfs(graph, start, visited, dfs_result)
bfs(graph, start, visited)

print(" ".join(str(x) for x in dfs_result))
print(" ".join(str(x) for x in bfs_result))