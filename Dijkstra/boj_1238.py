# boj 1238
# https://www.acmicpc.net/problem/1238

import sys
import heapq
INF = int(1e9)

n, m, x = map(int, sys.stdin.readline().split())
road = [[] for _ in range(m)]

for _ in range(m):
	a, b, c = map(int, sys.stdin.readline().split())
	road[a].append((b, c))

def dijkstra(start):
	q = []
	distance = [INF] * (n + 1)
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, current = heapq.heappop(q)
		if distance[current] < dist:
			continue
		for i in road[current]:
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

	return distance


from = dijkstra(x)
print(distance)
print(max(distance[1:]))