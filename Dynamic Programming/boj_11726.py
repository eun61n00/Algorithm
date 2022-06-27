# boj 11726 2×n 타일링
# 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

import sys
input = sys.stdin.readline

def tile(n):

	dp = [0] * 1001
	dp[1] = 1
	dp[2] = 2

	for idx in range(3, n+1):
		dp[idx] = dp[idx - 1] + dp[idx - 2]
	return dp[n]

if __name__ == '__main__':
	n = int(input())
	print(tile(n) % 10007)