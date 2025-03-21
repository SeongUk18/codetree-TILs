N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

candy_dict = {}

for i in range(N):
    if pos[i] in candy_dict:
        candy_dict[pos[i]] += candy[i]
    else:
        candy_dict[pos[i]] = candy[i]

max_candy = float('-inf')
# print(candy_dict)
# print(max(pos))
for i in range(100):
    count = 0
    for j in range(i, i + (2 * K) + 1):
        if j in candy_dict:
            count += candy_dict[j]
    max_candy = max(max_candy, count)

print(max_candy)
    