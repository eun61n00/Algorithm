from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
            continue

        if nx == n - 1 and y == m - 1:
            queue.clear()

        if graph[nx][ny] == 1:      # 방문하지 않았으면
            graph[nx][ny] = graph[x][y] + 1     # 방문 처리(최소 이동 횟수 카운트)
            queue.append((nx, ny))

print(graph[n - 1][m - 1])
