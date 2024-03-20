n = int(input())

way = ["" for _ in range(n * 200)]
start = int(len(way) / 2)

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == "R":
        for i in range(x):
            way[start + i] += "B"
        start += x
    else:
        for i in range(1, x + 1):
            way[start - i] += "W"
        start -= x

black = 0
white = 0
gray = 0
for i in way:
    if len(i) > 3:
        gray += 1
    elif i:
        if i[-1] == "W":
            white += 1
        elif i[-1] == "B":
            black += 1
        

print(f"{white} {black} {gray}")