n = int(input())

n_list = list(map(int, input().split()))
answer = 100000
for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(i - j) * n_list[j]
    answer = min(answer, dist)

print(answer)