# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14584 암호 해독

string = input()
n = int(input())
words = []
for _ in range(n):
    words.append(input())

for i in range(1, 26):
    decode = ''.join([chr(ord(c) + i) if ord(c) + i < 97+26 else chr(ord(c) + i - 26)  for c in string])
    for word in words:
        if word in decode:
            print(decode)
            exit(0)