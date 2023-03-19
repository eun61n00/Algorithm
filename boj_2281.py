# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2281 데스노트

import sys
input = sys.stdin.readline

n, w = map(int, input().split())
names = []
for i in range(n):
    names.append(int(input().rstrip()))

