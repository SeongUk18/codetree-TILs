x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

def solve():
    if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
        return "nonoverlapping"
    else:
        return "overlapping"

print(solve())