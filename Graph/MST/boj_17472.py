# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 17472 다리 만들기 2

import sys
input = sys.stdin.readline
n = int(input().rstrip())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

