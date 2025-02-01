from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))

total_sum = sum(arr)
min_diff = float('inf')
for i, j in combinations(range(N), 2):
    new_sum = total_sum - (arr[i] + arr[j])
    min_diff = min(min_diff, abs(S - new_sum))

print(min_diff)
