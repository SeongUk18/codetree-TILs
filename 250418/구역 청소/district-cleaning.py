a, b = map(int, input().split())
c, d = map(int, input().split())

if b > c or a < d:
    print(max(b, d) - min(a, c))
else:
    print(b - a + d - c)