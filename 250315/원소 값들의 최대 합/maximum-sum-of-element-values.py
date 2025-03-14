n, m = map(int, input().split())
arr = list(map(int, input().split()))

max_sum = float('-inf')
for i in range(1, n + 1):
    n_dict = {k + 1 : arr[k] for k in range(n)}
    start = i
    point = 0
    for _ in range(m):
        next = n_dict[start]
        # print(start, n_dict[start])
        # print(next, n_dict[next])
        point += next
        n_dict[start], n_dict[next] = n_dict[next], n_dict[start]
        # print(next)
        # print(start)
        # print(point)
    # print(point)
    # print("---")
    max_sum = max(max_sum, point)

print(max_sum)