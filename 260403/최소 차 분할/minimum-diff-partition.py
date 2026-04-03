n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)
dp = [False] * (total + 1)
dp[0] = True

for num in arr:
    for i in range(total, num - 1, -1):
        if dp[i - num]:
            dp[i] = True

# print(dp)

min_diff = total
for i in range(1, total):
    if dp[i]:
        diff = abs(i - (total - i))
        
        if diff < min_diff:
            min_diff = diff

print(min_diff)