# boj_1916.py
# https://www.acmicpc.net/problem/1916

import sys
import heapq
INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
distance =[INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
	a, b, c = map(int, sys.stdin.readline().split())
	graph[a].append((b, c))

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, current = heapq.heappop(q)
		if distance[current] < dist:
			continue

		for i in graph[current]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])

