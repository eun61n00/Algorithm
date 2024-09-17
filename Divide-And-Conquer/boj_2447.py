# -*- coding: utf-8 -*-
# boj 2447 별찍기-10

n = int(input())
star = [[] for _ in range(3 ** n)]
pattern = "***\n* *\n***"

def draw_star(idx):
	if idx > 3:
		draw_star(idx/3)
		draw_star(idx/3*2)
		draw_star(idx)
	else:
		star[idx-3].append('***')
		star[idx-2].append('* *')
		star[idx-1].append('***')

draw_star(n)
print(star)