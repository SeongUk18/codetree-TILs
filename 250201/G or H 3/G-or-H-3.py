n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

pic_dict = {}
for i in range(n):
    pic_dict[x[i]] = c[i]

max_num = float('-inf')
for i in range(1, max(x) + 1):
    point = 0
    for j in range(k + 1):
        if i + j in pic_dict:
            # print(pic_dict[i + j], i + j)
            if pic_dict[i + j] == "G":
                point += 1
            else:
                point += 2
    # print(point)
    max_num = max(max_num, point)

print(max_num)