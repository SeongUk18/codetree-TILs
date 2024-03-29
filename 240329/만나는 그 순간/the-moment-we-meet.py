n, m = map(int, input().split())

A = [0 for _ in range(2001)]
B = [0 for _ in range(2001)]
start = 1000
cnt = 1
for _ in range(n):
    commend, move = input().split()
    move = int(move)
    if commend == "R":
        for i in range(1, move + 1):
            A[start + i] = cnt
            cnt += 1
        start += move
    else:
        for i in range(1, move + 1):
            A[start - i] = cnt
            cnt += 1
        start -= move


start = 1000
cnt = 1
for _ in range(m):
    commend, move = input().split()
    move = int(move)
    if commend == "R":
        for i in range(1, move + 1):
            B[start + i] = cnt
            cnt += 1
        start += move
    else:
        for i in range(1, move + 1):
            B[start - i] = cnt
            cnt += 1
        start -= move


answer = n * m
for i in range(len(A)):
    if A[i] == B[i] and A[i] != 0:
        answer = min(A[i], answer)

print(answer)