# -*- coding: utf-8 -*-
# boj 1427 소트 인사이드

import sys
input = sys.stdin.readline

array = input().strip()
for i in range(9, -1, -1):
	for num in array:
		if i == int(num):
			print(num, end='')