a, b, c, d = map(int, input().split())

hour = c - a
minute = d - b

print(hour * 60 + minute)