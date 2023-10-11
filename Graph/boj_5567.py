# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 5567 결혼식

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

friends = []

for friend in graph[1]:
    friends.append(friend)
    for friend_of_friend in graph[friend]:
        friends.append(friend_of_friend)

if 1 in friends:
    friends = set(friends)
    friends.remove(1)
    print(len(friends))
else:
    print(len(set(friends)))
