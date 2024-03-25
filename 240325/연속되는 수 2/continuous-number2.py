n = int(input())

answer = []
cnt = 0
before = 123456789
for i in range(n):
    number = int(input())
    if i == 0 or before == number:
        cnt += 1
        before = number
    else:
        answer.append(cnt)
        cnt = 1
        before = number

print(max(answer))