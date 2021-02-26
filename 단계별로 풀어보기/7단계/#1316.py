n = int(input())
word_list = []
for i in range(n):
    word = input()
    word_list.append(word)

for i in range(len(word_list)):
    while j in word_list[i]:
        word_list = word_list.replace(j, "", 1)

def count_group_word(list):
    return sum(list)
