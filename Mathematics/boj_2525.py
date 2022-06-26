# boj 2525
# https://www.acmicpc.net/problem/2525

import sys

hour, min = map(int, sys.stdin.readline().split())
required = int(sys.stdin.readline())

min += required
hour += (min / 60)
min %= 60
hour %= 24

print(int(hour), int(min))