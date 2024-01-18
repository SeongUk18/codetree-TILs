n, m = map(int, input().split())

dic1 = {}
dic2 = {}

for i in range(1, n + 1):
    val = input()
    dic1[str(i)] = val
    dic2[val] = str(i)

for _ in range(m):
    find_word = input()
    if find_word in dic1:
        print(dic1[find_word])
    else:
        print(dic2[find_word])