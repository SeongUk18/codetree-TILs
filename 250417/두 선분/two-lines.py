x1, x2, x3, x4 = map(int, input().split())

x_list = list(range(x1, x2 + 1))
y_list = list(range(x3, x4 + 1))

def solve():
    for x in x_list:
        if x in y_list:
            print("intersecting")
            return

    print("nonintersecting")

solve()
