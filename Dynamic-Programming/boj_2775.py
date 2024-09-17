# -*- coding: utf-8 -*-
# boj2775 부녀회장이 될테야

import sys
input = sys.stdin.readline

def get_value(arr, k, n):
    arr[k][n] = 0
    for i in range(n):
        arr[k][n] += arr[k - 1][n]

if __name__ == "__main__":

    test_case = int(input());

    for i in range(test_case):
        k = int(input());
        n = int(input());
        arr = [[i + 1 for i in range(n)] for _ in range(k + 1)]

        for i in range(1, k + 1):
            for j in range(1, n):
                get_value(arr, i, j)
        
        print(arr)
        print(arr[k][n - 1])