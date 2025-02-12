N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.sort()

max_num = float('-inf')
for i in range(N):
    cost = 0
    num = 0
    for j in range(N):
        if i == j:
            cost += P[j] / 2
        else:
            cost += P[j]

        if cost <= B:
            num += 1
            # print(cost, num)
    max_num = max(max_num, num)
    
    
print(max_num)