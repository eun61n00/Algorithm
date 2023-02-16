# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 6550 부분 문자열

while True:
    try:
        s, t = map(str, input().split())

        flag = 0
        idx = 0
        for ch in t:
            if ch == s[idx]:
                idx += 1

            if idx == len(s):
                flag = 1
                break
        if flag == 1:
            print("Yes")
        else:
            print("No")

    except:
        break