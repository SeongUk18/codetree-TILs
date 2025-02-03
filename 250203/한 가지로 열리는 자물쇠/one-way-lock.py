N = int(input())
a, b, c = map(int, input().split())

count = 0
for i in range(1, N + 1):
    if i - 2 <= a <= i + 2:
        continue
    else:
        for j in range(1, N + 1):
            if j - 2 <= b <= j + 2:
                continue
            else:
                for k in range(1, N + 1):
                    if k - 2 <= c <= k + 2:
                        continue
                    else:
                        count += 1

answer = N * N * N - count
print(answer)
                        