N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_count = float('-inf')
for i in range(N):
    min_num = arr[i]
    max_num = arr[i]
    new_arr = [arr[i]]
    for j in range(N):
        if i == j:
            continue

        min_num = min(min(new_arr), arr[j])
        max_num = max(max(new_arr), arr[j])

        if max_num - min_num <= K:
            new_arr.append(arr[j])
        # print(min_num, max_num)
        # print(new_arr)
    max_count = max(max_count, len(new_arr))

print(max_count)
