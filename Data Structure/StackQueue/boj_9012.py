# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 9012 괄호

n = int(input())


def check_parenthesis_string(string):
    stack = []
    for ch in string:
        if stack and ch == ")" and stack[-1] == "(":
            stack.pop(-1)
            continue
        else:
            stack.append(ch)
    if stack:
        return "NO"
    else:
        return "YES"


for _ in range(n):
    string = input()
    print(check_parenthesis_string(string))
