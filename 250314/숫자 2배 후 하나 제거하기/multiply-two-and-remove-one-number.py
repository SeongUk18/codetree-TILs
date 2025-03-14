import copy

n = int(input())
arr = list(map(int, input().split()))

min_dist = float('inf')
for i in range(n):
    new_arr = copy.deepcopy(arr)
    new_arr[i] = arr[i] * 2
    # print(new_arr)
    for j in range(n):
        # print(new_arr)
        temp_arr = new_arr[:j] + new_arr[j + 1:]
        # print(temp_arr) 

        dist = 0
        for k in range(1, len(temp_arr)):
            dist += abs(temp_arr[k] - temp_arr[k - 1])
        min_dist = min(min_dist, dist)

print(min_dist)