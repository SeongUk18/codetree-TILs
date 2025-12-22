a = list(map(int, input().split()))

# Please write your code here.
dist = max(a[1] - a[0], a[2] - a[1])

if dist == 1:
    print(0)
else:
    print(dist - 1)