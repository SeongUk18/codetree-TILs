n, k = map(int, input().split())
arr = list(map(int, input().split()))

max_num = float('-inf')
for i in range(n - k + 1):
    num = sum(arr[i:i + k])
    max_num = max(max_num, num)

print(max_num)