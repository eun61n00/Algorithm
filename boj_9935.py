# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 9935 문자열 폭발

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

str = deque(list(input().strip()))
bomb = input().strip()

str_dict = defaultdict(list)

for i, ch in enumerate(str):
    str_dict[i].append(ch)

while bomb in str:
    remove = ""
    for i in range(len(str)):
        ch = str.popleft()
        if ch == bomb[0]:
            remove += ch
            if remove == bomb:

        else:
            str.append(ch)


    for i in range(len(str) - len(bomb) + 1):
        if str[i : i+len(bomb)] == bomb:
            str = str[0:i] + str[i+len(bomb):]

if not str:
    print("FRULA")
else:
    print(str)