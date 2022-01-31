import collections
word = input()
word = word.upper()
c = collections.Counter(word)
answer = c.most_common()
if len(answer) == 1:
    print(answer[0][0])
elif answer[0][1] == answer[1][1]:
    print ('?')
else:
    print(answer[0][0])
