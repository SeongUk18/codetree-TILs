from itertools import combinations

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

dic = {}
answer = 0

for i in range(n):
    for j in range(1 + i, n):
        sum_num = numbers[i] + numbers[j]
        if sum_num in dic:
            dic[sum_num].append((i, j))
        else:
            dic[sum_num] = [(i, j)]

for i in range(n):
    target = m - numbers[i]
    if target in dic:
        for j in dic[target]:
            if i not in j:
                answer += 1

answer = answer // 3

print(answer)