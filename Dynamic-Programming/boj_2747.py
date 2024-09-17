# -*- coding: utf-8 -*-
# boj2747 피보나치수2

import sys
input = sys.stdin.readline

def fibonacci(n):
	dp = [0] * 91
	dp[1] = 1

	for i in range(2, n + 1):
		dp[i] = dp[i - 2] + dp[i - 1]

	return dp[n]


if __name__ == '__main__':
	n = int(input())
	print(fibonacci(n))

