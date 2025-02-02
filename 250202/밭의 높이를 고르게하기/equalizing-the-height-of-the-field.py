N, H, T = map(int, input().split())
arr = list(map(int, input().split()))


height = H * T
min_diff = float('inf')

for i in range(N - T + 1):
    diff = 0
    for j in range(i, i + T):
        diff += abs(arr[j] - H)
    min_diff = min(diff, min_diff)

print(min_diff)