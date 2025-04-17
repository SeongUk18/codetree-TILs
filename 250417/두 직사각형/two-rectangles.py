x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

def solve():
    if x1 > a1 or x2 < a2:
        print("overlapping")
        return
    elif y1 > b1 or y2 < b2:
        print("overlapping")
        return
    
    print("nonoverlapping")

solve()