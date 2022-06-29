# -*- coding: utf-8 -*-
# boj 2750 수 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for i in range(n):
    user_input = int(input())
    numbers.append(user_input)
numbers.sort()
for i in numbers:
    print(i)