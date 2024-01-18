n = int(input())

dic = {}

for _ in range(n):
    color = input()
    if color in dic:
        dic[color] = dic[color] + 1
    else:
        dic[color] = 1

print(max(dic.values()))