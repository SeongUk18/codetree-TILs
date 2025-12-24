n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
mid = int(sum(blocks) / n)

answer = 0

for b in blocks:
    if b > mid:
        answer += (b - mid)

print(answer)