X, Y = map(int, input().split())

max_sum = 0
for i in range(X, Y + 1):
    i = str(i)
    sum = 0
    for j in i:
        sum += int(j)
    # print(i)
    max_sum = max(max_sum, sum)

print(max_sum)