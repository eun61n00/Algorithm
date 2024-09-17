# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 10816 숫자게임2

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
problems = list(map(int, input().split()))

number_dict = defaultdict(int)

for card in cards:
    number_dict[card] += 1

answer = []
for p in problems:
    answer.append(number_dict[p])

print(*answer)
