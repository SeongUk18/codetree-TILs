from itertools import combinations

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

dic = {}
answer = 0

for i in combinations(numbers, 3):
    if sum(i) == m:
        answer += 1


print(answer)