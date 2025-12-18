a, b, x, y = map(int, input().split())

# Please write your code here.

walk = abs(b - a)
tel_x = abs(x - a) + abs(y - b)
tex_y = abs(y - a) + abs(x - b)

min_dist = min(walk, tel_x, tex_y)

print(min_dist)