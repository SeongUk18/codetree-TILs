from itertools import combinations

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
num = 0
for i in combinations(numbers, 2):
    if sum(i) == m:
        num += 1

print(num)