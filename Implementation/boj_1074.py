# -*- coding: utf-8 -*-
# boj 1074 Z

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
arr = [[0] * (2 ** n)] * (2 ** n)

num = 0

def z(array, num):
	if len(array) < 3:
		array[0][0] = num
		num += 1
		array[0][1] = num
		num += 1
		array[1][0] = num
		num += 1
		array[1][1] = num
		num += 1
		return num, array

	mid = int(len(array) // 2)
	arr_1, arr_2, arr_3, arr_4 = [line[:mid] for line in array[:mid]], [row[:mid] for row in array[mid:]], \
			[row[mid:] for row in array[:mid]], [row[mid:] for row in array[mid:]]
	num, arr_1  = z(arr_1, num)
	num, arr_2  = z(arr_2, num)
	num, arr_3  = z(arr_3, num)
	num, arr_4  = z(arr_4, num)
	return num, arr_1 + arr_2 + arr_3 + arr_4
z(arr, num)
print(arr)
