# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 같은 숫자는 싫어

def solution(arr):
    stack = []
    for elem in arr:
        if stack[-1] == elem:
            continue
        else:
            stack.append(elem)
    return stack