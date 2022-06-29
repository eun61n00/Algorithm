# -*- coding: utf-8 -*-
# boj 10814 좌표 정렬

import sys
input = sys.stdin.readline

n = int(input())
map_arr = list()
for _ in range(n):
	x, y = map(int, input().split())
	map_arr.append((x, y))

map_arr = sorted(map_arr)

for i in map_arr:
	print(i[0], i[1])
