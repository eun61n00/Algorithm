# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 9935 문자열 폭발

import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
str = deque(list((input().strip())))
stack = []
bomb = list(input().strip())
check = True

while str:
    ch = str.popleft()
    stack.append(ch)
    if ch == bomb[-1] and stack[-len(bomb):] == bomb:
        for i in range(len(bomb)):
            stack.pop()

if not stack:
    print("FRULA")
else:
    print(''.join(stack))