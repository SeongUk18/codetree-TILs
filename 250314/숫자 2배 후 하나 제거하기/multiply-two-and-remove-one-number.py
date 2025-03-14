import copy

n = int(input())
arr = list(map(int, input().split()))

min_dist = float('inf')
for i in range(n):
    new_arr = copy.deepcopy(arr)
    new_arr[i] = arr[i] * 2
    # print(new_arr)
    for j in range(n):
        if i == j:
            continue
        prev = False
        prev_num = 0
        # print(new_arr)
        for k in range(n):
            if j == k:
                continue
            if prev == False:
                prev_num = new_arr[k]
                prev = True
                dist = 0
            else:
                dist += abs(prev_num - new_arr[k])
                # print(j)
                # print(prev_num, new_arr[k])
                # print(dist)
        min_dist = min(min_dist, dist)

print(min_dist)