# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2149 암호 해독

# HUMDING
# EIAAHEBXOIFWEHRXONNAALRSUMNREDEXCTLFTVEXPEDARTAXNAARYIEX

from collections import defaultdict

key = input()
string = input()

string_list = []

for idx, ch in enumerate(key):
    lst = [ch]
    for i in range(len(string) // len(key)):
        lst.append(string[idx + len(key) + i])
    string_list.append(lst)

string_list = sorted(string_list)

for col in range(1, len(key)):
    for row in range(len(string_list)):
        print(string_list[row][col], end='')
