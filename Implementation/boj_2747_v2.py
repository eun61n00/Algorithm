# -*- coding: utf-8 -*-
# boj 2747 피보나치 수
# Time OUT***

import sys
input = sys.stdin.readline

n = int(input())

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(n))