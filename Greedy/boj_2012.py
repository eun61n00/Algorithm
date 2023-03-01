# usr/bin/env python
# -*- coding: utf8 -*-
# boj 2012 등수 매기기

import sys

input = sys.stdin.readline

n = int(input().rstrip())
excepted = sorted([int(input()) for _ in range(n)])
ranks = [i for i in range(1, n + 1)]

answer = 0
for i in range(n):
    answer += abs(excepted[i] - ranks[i])

print(answer)