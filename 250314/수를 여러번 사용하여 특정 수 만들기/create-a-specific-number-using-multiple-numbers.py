A, B, C = map(int, input().split())

# Please write your code here.
max_num = float('-inf')

for i in range(C // A + 1):
    num = i * A

    while num <= C:
        if C >= num + B:
            num += B
        else:
            break

    max_num = max(num, max_num)

print(max_num)