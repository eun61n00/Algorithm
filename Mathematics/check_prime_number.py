# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 소수 판별 알고리즘

import math


# 1. 완전 탐색 방법
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 2. 제곱근까지만 확인하는 방법
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# 3. 에라토스테네스의 체 (Sieve of Eratosthenes)
n = 1000    # 2부터 1000까지의 모두 수에 대하여 소수 판별
array = [True for i in range(n + 1)]    # 소수인지 아닌지 판별한 값을 담는 배열(0과 1은 소수가 아님)

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:     # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모두 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
