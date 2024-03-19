n, k = map(int, input().split())

block_list = [0 for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(b - a + 1):
        block_list[a + i] += 1

print(max(block_list))