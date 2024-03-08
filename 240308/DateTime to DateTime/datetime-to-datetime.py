a, b, c = map(int, input().split())


if a < 11 or (a == 11 and b < 11) or (a == 11 and b == 11 and c < 11):
    answer = -1
else:
    day = a - 11
    hour = b - 11
    minute = c - 11
    answer = day * 1440 + hour * 60 + minute

print(answer)