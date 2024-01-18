from itertools import combinations

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
num = 0
num_list = []

for i in combinations(numbers, 2):
    if i in num_list:
        num += 1
    elif sum(i) == m:
        num += 1

print(num)