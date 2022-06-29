# -*- coding: utf-8 -*-
# boj 2747 피보나치 수
# 재귀 함수아닌 단순 반복문으로 풀이

import sys
input = sys.stdin.readline

n = int(input())
a, b = 0, 1

while n > 0:
	a, b = b, a + b
	n -= 1

print(a)
