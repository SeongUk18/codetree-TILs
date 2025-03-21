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


answer = 0
for i in range(10, 0, -1):
    num = i

    if find(num):
        answer = i

print(answer)    