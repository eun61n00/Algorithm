# -*- coding: utf-8 -*-
# boj 9095 1,2,3 더하기

import sys
input = sys.stdin.readline

def sum_123(n):
	dp = [0] * 11
	dp[1] = 1
	dp[2] = 2
	dp[3] = 4

	for i in range(4, n + 1):
		dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

	return dp[n]

if __name__ == '__main__':
	test_case = int(input())
	for _ in range(test_case):
		n = int(input())
		print(sum_123(n))