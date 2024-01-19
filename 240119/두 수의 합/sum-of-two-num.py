# 조합으로 풀이하려고 했지만 시간 초과로 풀이 방법 변경
# from itertools import combinations

# n, m = map(int, input().split())

# numbers = list(map(int, input().split()))
# num = 0
# num_list = []

# for i in combinations(numbers, 2):
#     if i in num_list:
#         num += 1
#     elif sum(i) == m:
#         num += 1

# print(num)

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

dic = {}
answer = 0

for i in numbers:
    target = m - i

    if target in dic:
        answer += dic[target]

    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(answer)