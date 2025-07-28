# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11501 주식

import sys

input = sys.stdin.readline


def solution(n, prices):
    answer = 0
    max = prices[-1]
    for price in reversed(prices[:-1]):
        if max > price:
            answer += (max - price)
        else:
            max = price
    return answer


t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    print(solution(n, prices))
