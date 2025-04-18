from collections import defaultdict

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

num_dict = defaultdict(int)


for i in range(n):
    for j in range(x1[i], x2[i] + 1):
        num_dict[j] += 1

if max(num_dict.values()) == n:
    print("Yes")
else:
    print("No")