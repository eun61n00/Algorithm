# -*- coding: utf-8 -*-
# boj 1074 Z

import sys
input = sys.stdin.readline

def z_solve(n, x, y):
	global num
	if n == 2:
		if x == r and y == c :
			print(num)
			return
		num += 1
		if x == r and y + 1 == c:
			print(num)
			return
		num += 1
		if x + 1 == r and y == c:
			print(num)
			return
		num += 1
		if x + 1 == r and y + 1 == c:
			print(num)
			return
		num += 1
		return
	if r < n/2 and c <= n/2:
		z_solve(n/2, x, y)
	num += (n/2)*4
	if r >= n/2 and  c <= n/2:
		z_solve(n/2, x + (n / 2), y)
	num += (n/2)*4
	if r < n/2 and c >= n/2:
		z_solve(n/2, x, y + (n / 2))
	num += (n/2)*4
	if r >= n/2 and c >= n/2:
		z_solve(n/2,  x + (n / 2), y + (n / 2))
	num += (n/2)*4

n, r, c = map(int, input().split())
num = 0
z_solve(2 ** n, 0, 0)