# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1629

from copy import deepcopy
from sys import stdin

input = stdin.readline


# a의 b제곱을 c로 나눈 나머지를 계산하는 함수
def fun(a, b, c):
    if b == 1:
        return a % c
    tmp = fun(a, b // 2, c)
    if b % 2 == 0:
        return (tmp * tmp) % c
    else:
        return (tmp * tmp * a) % c


a, b, c = map(int, input().split())
print(fun(a, b, c))
