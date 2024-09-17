# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 5430 AC

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    p.replace("RR", "")
    p = list(p)
    n = int(input())
    array = deque(eval(input()))

    if p.count("D") > len(array):
        print("error")
        continue

    direction = 1
    for f in p:
        if f == 'R':
            direction *= -1
        elif f == 'D':
            if len(array) == 0:
                print("error")
                break
            if direction == 1:
                array.popleft()
                # array = array[1:]
            else:
                array.pop()
                # array = array[:-1]
    if direction == -1:
        array.reverse()
    print(str(list(array)).replace(' ', ''))
