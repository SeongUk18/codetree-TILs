n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.
jobs.sort()
# print(jobs)

dp = [0] * n
dp[0] = jobs[0][2]

for i in range(n):
    for j in range(i + 1, n):
        if jobs[i][1] < jobs[j][0]:
            dp[j] = max(dp[i] + jobs[j][2], dp[i])
        else:
            dp[j] = max(dp[i], jobs[j][2])

print(max(dp))