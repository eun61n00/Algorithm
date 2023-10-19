# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 13458


import sys

input = sys.stdin.readline
n = int(input())
students = list(map(int, input().split()))

director1, director2 = map(int, input().split())
answer = 0

students = [n - director1 if n >= director1 else 0 for n in students]
print(sum([n//director2 if n % director2 == 0 else n //
           director2 + 1 for n in students]) + n)
