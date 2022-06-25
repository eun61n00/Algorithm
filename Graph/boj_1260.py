# boj_1260) DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())

def dfs(graph, v, visited, dfs_res):
	visited[v] = True
	dfs_res.append(v)

	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited, dfs_res)


def bfs(graph, v, visited):
	queue = deque([start])
	visited[start] = True
	bfs_res = []

	while queue:
		v = queue.popleft()
		bfs_res.append(v)

		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
	return bfs_res


graph = [[] for _ in range(n + 1)]
for _ in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

for edge in graph:
	edge = edge.sort()

visited = [False] * (n + 1)
dfs_res = []
dfs(graph, start, visited, dfs_res)
print(' '.join(str(i) for i in dfs_res))

visited = [False] * (n + 1)
bfs_res = bfs(graph, start, visited)
print(' '.join(str(i) for i in bfs_res))