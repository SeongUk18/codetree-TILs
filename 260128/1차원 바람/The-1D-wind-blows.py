n, m, q = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
winds = [(int(r), d) for r, d in [input().split() for _ in range(q)]]

# Please write your code here.
def check_same_num(m, start, pos):
    for i in range(m):
        if a[start + pos][i] == a[start][i]:
            return True
    return False


def shift_row(i, dir):
    if dir == "L":
        end = a[i][-1]
        new = a[i][:]
        for j in range(1, m):
            a[i][j] = new[j - 1]
        a[i][0] = end
    else:
        start = a[i][0]
        new = a[i][:]
        for j in range(m - 1):
            a[i][j] = new[j + 1]
        a[i][-1] = start
    # print(i, a[i])


for row, dir in winds:
    row -= 1
    shift_row(row, dir)

    if dir == "L":
        next_dir = "R"
    else:
        next_dir = "L" 

    next = row

    while next - 1 >= 0:
        if check_same_num(m, next, -1):
            next = next - 1

            shift_row(next, next_dir)
            if next_dir == "L":
                next_dir = "R"
            else:
                next_dir = "L" 
        else:
            break

    if dir == "L":
        next_dir = "R"
    else:
        next_dir = "L"

    next = row

    while next + 1 <= n - 1:
        if check_same_num(m, next, 1):
            next = next + 1

            shift_row(next, next_dir)
            if next_dir == "L":
                next_dir = "R"
            else:
                next_dir = "L" 
        else:
            break


for i in range(n):
    for j in range(m):
        print(a[i][j], end=" ")
    print()