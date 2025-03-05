X, Y = map(int, input().split())

def check(n):
    str_n = str(n)
    reversed_str_n = ''.join(list(reversed(str_n)))
    # print(str_n, reversed_str_n)
    if str_n == reversed_str_n:
        return True
    else:
        return False

answer = 0
for i in range(X, Y + 1):
    if check(i):
        answer += 1

print(answer)