X, Y = map(int, input().split())


def check(num):
    num_str = str(num)
    start = num_str[0]
    count = 0
    str_set = set()
    for s in num_str:
        if start != s:
            count += 1
        str_set.add(s)

    if count == 1 or count == len(num_str) - 1 and len(str_set) == 2:
        # print(num_str)
        return True

    else:
        return False

answer = 0
for i in range(X, Y + 1):
    if check(i):
        answer += 1

print(answer)