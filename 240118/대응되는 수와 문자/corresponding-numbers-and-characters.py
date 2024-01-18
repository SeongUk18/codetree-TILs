n, m = map(int, input().split())

dic = {}

for i in range(1, n + 1):
    val = input()
    dic[str(i)] = val

for _ in range(m):
    find_word = input()
    if find_word in dic:
        print(dic[find_word])
    else:
        print(list(dic.values()).index(find_word) + 1)