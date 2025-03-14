import copy

n = int(input())
arr = list(map(int, input().split()))

min_dist = float('inf')
for i in range(n):
    new_arr = copy.deepcopy(arr)
    # print(new_arr)
    new_arr[i] = arr[i] * 2

    for j in range(n):
        dist = 0
        prev = False
        prev_num = 0
        for k in range(n):
            if j == k:
                continue
            if prev == False:
                prev_num = new_arr[k]
                prev = True
            else:
                dist += abs(prev_num - new_arr[k])
                # print(prev_num, new_arr[k])
                # print(dist)
        min_dist = min(min_dist, dist)

print(min_dist)