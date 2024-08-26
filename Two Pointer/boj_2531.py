# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2531 회전초밥

from collections import deque, defaultdict
import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = []
for _ in range(n):
    belt.append(int(input()))

# Use a dictionary to track the number of each type of sushi in the window
window = defaultdict(int)

# Initialize the first window
for i in range(k):
    window[belt[i]] += 1

# Add the coupon sushi
window[c] += 1
answer = len(window)

# Slide the window across the belt
for i in range(1, n + 1):
    window[belt[i - 1]] -= 1
    if window[belt[i - 1]] == 0:
        del window[belt[i - 1]]
    # Add the new sushi that enters the window
    window[belt[(i + k - 1) % n]] += 1
    # Update the maximum number of unique sushis
    answer = max(len(window), answer)

print(answer)
