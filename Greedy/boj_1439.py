# usr/bin/env python
# -*- coding: utf8 -*-
# boj 1439 거스름돈

import sys

input = sys.stdin.readline
s = list(input())

zero_group = 0
one_group = 0

if len(s) == 1:
    print(1)
    exit()

cur = s[0]
for i in s[1:]:
    if cur != i:
        if cur == '0':
            zero_group += 1
        else:
            one_group += 1
    cur = i

print(min(zero_group, one_group))