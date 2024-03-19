n = int(input())

way = [0 for _ in range(2001)]

start = 1000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == "R":
        for i in range(x):
            way[start + i] += 1
        start += x
    else:
        for i in range(1, x + 1):
            way[start - i] += 1
        start -= x

answer = len([x for x in way if x >= 2])

print(answer)