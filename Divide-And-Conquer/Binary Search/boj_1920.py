# -*- coding: utf-8 -*-
# boj 1920 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
num_list = set(map(int, input().split()))

test_case = int(input())
test_num = list(map(int, input().split()))

for num in test_num:
	if num in num_list:
		print('1')
	else:
		print('0')
