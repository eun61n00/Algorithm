# -*- coding: utf-8 -*-
# boj 1181 단어 정렬

import sys
input = sys.stdin.readline


def quick_sort(word_dict):

	if len(word_dict) <= 1:
		return word_dict

	pivot = num_list[0]
	left = [item for item in num_list[1:] if item < pivot]
	right = [item for item in num_list[1:] if item > pivot]


	return left + [pivot] + right


if __name__ == '__main__':
	case = int(input())
