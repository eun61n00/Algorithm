# -*- coding: utf-8 -*-
# boj 1427 소트 인사이드

import sys
input = sys.stdin.readline

num = input().strip()
num_arr = []
for chr in num:
	num_arr.append(int(chr))

num_arr.sort(reverse=True)
for num in num_arr:
	print(num, end='')