n = int(input())

way = [0 for _ in range(1000)]

start = 0

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == "R":
        for i in range(x):
            start += 1
            way[start] += 1
    else:
        for i in range(x):
            start -= 1
            way[start] += 1

answer = len([x for x in way if x >= 2])

print(answer)