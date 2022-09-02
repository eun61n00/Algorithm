# -*- coding: utf-8 -*-

import sys
input = sys.stdin.realine

n = int(input())
car_info = dict()
ans = 0

for i in range(1, n + 1):
	v, w = map(int, input().split())
	if v in car_info.keys():
		if w > car_info[v][1]:
			car_info[v] = [i, w]
		else:
			car_info[v] = [i, w]

	for i in car_info.values():
		ans += i[0]

print(ans)