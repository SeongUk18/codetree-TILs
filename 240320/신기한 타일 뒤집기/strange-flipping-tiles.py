n = int(input())

way = ["" for _ in range(n * 200)]
start = int(len(way) / 2)

for _ in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == "R":
        for i in range(x):
            way[start + i] = "R"
        start += x - 1
    else:
        for i in range(x):
            way[start - i] = "L"
        start -= x - 1

black = way.count("R")
white = way.count("L")

print(f"{white} {black}")