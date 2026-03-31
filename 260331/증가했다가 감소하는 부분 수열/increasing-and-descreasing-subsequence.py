n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
dp = [1] * n

for i in range(n):
    count = 0
    flag = 'same'

    for j in range(i + 1, n):
        if sequence[i] > sequence[j] and flag != 'up':
            count += 1
            flag = 'up'

        elif sequence[i] < sequence[j] and flag != 'down':
            count += 1
            flag = 'down'

        if count == 2:
            dp[j] = max(dp[i] + j - i, j - i)

print(max(dp))