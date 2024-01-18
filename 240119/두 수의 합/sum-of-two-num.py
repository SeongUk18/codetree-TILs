from itertools import combinations

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
num = 0
dic = {}

for i, j in combinations(numbers, 2):
    if i and j in dic:
        num += 1
    elif i + j == m:
        dic[i] = j
        dic[j] = i
        num += 1

print(int(num/2))