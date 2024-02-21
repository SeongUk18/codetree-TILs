from sortedcontainers import SortedDict

n = int(input())

word_dic = SortedDict()

for _ in range(n):
    word = input()
    if word in word_dic:
        word_dic[word] += 1
    else:
        word_dic[word] = 1

for k, v in word_dic.items():
    print("{} {}".format(k, v))