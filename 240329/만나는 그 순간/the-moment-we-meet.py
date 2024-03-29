n, m = map(int, input().split())

A = [0 for _ in range(2001)]
B = [0 for _ in range(2001)]
start = 1000
cnt = 1
for _ in range(n):
    commend, move = input().split()
    move = int(move)
    if commend == "R":
        for i in range(move):
            A[start + i] = cnt
            start += move
            cnt += 1
    else:
        for i in range(move):
            A[start - i] = cnt
            start -= move
            cnt += 1


start = 1000
cnt = 1
for _ in range(m):
    commend, move = input().split()
    move = int(move)
    if commend == "R":
        for i in range(move):
            B[start + i] = cnt
            start += move
            cnt += 1
    else:
        for i in range(move):
            B[start - i] = cnt
            start -= move
            cnt += 1


answer = n * m
for i in range(len(A)):
    if A[i] == B[i] and A[i] != 0:
        answer = min(A[i], answer)

print(answer)