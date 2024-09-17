# boj 9461 파도반 수열
# https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

def padovan(n):
	dp = [1] * (n + 1)
	dp[0] = 0
	for idx in range(3, n + 1):
		dp[idx] = dp[idx-3] + dp[idx-2]

	return dp[n]


if __name__ == "__main__":
	cnt = int(input())
	for _ in range(cnt):
		n = int(input())
		print(padovan(n))
