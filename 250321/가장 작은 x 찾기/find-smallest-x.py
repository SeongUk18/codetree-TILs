n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]

def find(num):
    for a, b in ranges:
        num *= 2
        # print(num)
        if a <= num and num <= b:
            continue
        else:
            return False
    return True

start, end = ranges[0]
answer = 0
for i in range(end // 2, start // 2, -1):
    num = i

    if find(num):
        answer = i

print(answer)    