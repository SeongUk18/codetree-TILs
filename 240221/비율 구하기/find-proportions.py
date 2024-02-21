from sortedcontainers import SortedDict

color_dic = SortedDict()

n = int(input())

for _ in range(n):
    color = input()
    if color in color_dic:
        color_dic[color] += 1
    else:
        color_dic[color] = 1

sum_num = sum(list(color_dic.values()))

for k, v in color_dic.items():
    answer = round(v/sum_num*100, 5)
    print("{} {:.4f}".format(k, answer))