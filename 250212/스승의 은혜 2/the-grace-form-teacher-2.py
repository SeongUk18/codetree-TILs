N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.sort()

max_num = float('-inf')
for i in range(N):
    cost = 0
    num = 0
    for j in range(N):
        if i == j:
            num += 1
            cost += P[i] / 2
        else:
            num += 1
            cost += P[i]

        if cost > B:
            break
    max_num = max(max_num, num - 1)
    
if sum(P[:-1]) + P[-1] / 2 <= B:
    max_num = N
print(max_num)