# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def search(x, y):
	global score

	visited[x][y] = True
	if parking_map[x][y] == 2:
		score += -2
	elif parking_map[x][y] == 0:
		score += 1

	if y - 1 > -1 and visited[x][y - 1] == False:
		if parking_map[x][y - 1] == 2 or parking_map[x][y - 1] == 0:
			visited[x][y - 1] == True
			search(x, y - 1)
	if x - 1 > -1 and visited[x - 1][y] == False:
		if parking_map[x - 1][y] == 2 or parking_map[x - 1][y] == 0:
			visited[x - 1][y] == True
			search(x - 1, y)
	if y + 1 < m and visited[x][y + 1] == False:
		if parking_map[x][y + 1] == 2 or parking_map[x][y + 1] == 0:
			visited[x][y + 1] == True
			search(x, y + 1)
	if x + 1 < n and visited[x + 1][y] == False:
		if parking_map[x + 1][y] == 2 or parking_map[x + 1][y] == 0:
			visited[x + 1][y] == True
			search(x + 1, y)

	return


if __name__ == '__main__':
	n, m = map(int, input().split())
	parking_map = list()

	for _ in range(n):
		parking_map.append(list(map(int, input().split())))

	score_list = list()
	visited = [[False for _ in range(m)] for __ in range(n)]

	for x in range(n):
		for y in range(m):
			if (parking_map[x][y] == 2 or parking_map[x][y] == 0) and visited[x][y] == False:
				score = 0
				search(x, y)
				score_list.append(score)

	if max(score_list) < 0:
		print(0)
	else:
		print(max(score_list))