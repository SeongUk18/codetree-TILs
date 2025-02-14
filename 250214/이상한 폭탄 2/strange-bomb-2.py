N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

answer = -1

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if i - K <= j <= i + K and num[i] == num[j]:
            answer = max(answer, num[i])

print(answer)