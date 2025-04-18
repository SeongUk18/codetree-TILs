a, b = map(int, input().split())
c, d = map(int, input().split())

grid = [False for _ in range(101)]

answer = 0
for i in range(a, b):
    grid[i] = True

for i in range(c, d):
    grid[i] = True

for i in range(len(grid)):
    if grid[i]:
        answer += 1

print(answer)