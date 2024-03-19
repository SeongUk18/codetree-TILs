n = int(input())

answer_list = [0 for _ in range(201)]

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1 += 100
    x2 += 100
    for i in range(x2 - x1 + 1):
        answer_list[x1 + i] += 1

print(max(answer_list) - 1)
print(answer_list)