n = int(input())
numbers = list(map(int, input().split()))

max_num = float("-inf")

for i in range(n):
    num = 0
    for j in range(n):
        if j == i - 1 or j == i + 1 or i == j:
            continue
        
        num = numbers[i] + numbers[j]
        max_num = max(num, max_num)

print(max_num)