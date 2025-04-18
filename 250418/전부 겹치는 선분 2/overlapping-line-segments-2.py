from collections import defaultdict

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

check = False

for i in range(n):
    num_dict = defaultdict(int)
    for j in range(n):
        if i == j:
            continue

        for k in range(x1[j], x2[j] + 1):
            num_dict[k] += 1

    if max(num_dict.values()) == n - 1:
        check = True


if check:
    print("Yes")
else:
    print("No")