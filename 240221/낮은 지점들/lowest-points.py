n = int(input())

xy_dic = {}

for _ in range(n):
    x, y = map(int, input().split())
    if x in xy_dic:
        if xy_dic[x] > y:
            xy_dic[x] = y
    else:
        xy_dic[x] = y

answer_list = xy_dic.values()

print(sum(answer_list))