from collections import defaultdict

N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

num_dict = defaultdict(int)

# print(set(num))
for i in set(num):
    num_dict[i] = 1


for i in range(N):
    bomb = num[i]
    for j in range(i + 1, i + K + 1):
        if j >= N:
            break

        # print( num[j], bomb)
        if bomb == num[j]:
            num_dict[bomb] += 1
            break

# print(num_dict)

answer = sorted(num_dict.items(), key = lambda x : (- x[1], - x[0]))

# print(answer)

if answer[0][1] == 1:
    print(0)
else:
    print(answer[0][0])