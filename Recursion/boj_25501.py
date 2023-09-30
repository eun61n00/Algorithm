# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 25501

n = int(input())


def isPalindrome(word, s, e, count):
    if s >= e:
        return 1, count
    elif word[s] != word[e]:
        return 0, count
    else:
        count += 1
        return isPalindrome(word, s + 1, e - 1, count)


for _ in range(n):
    word = input()
    print(*isPalindrome(word, 0, len(word) - 1, 1))
