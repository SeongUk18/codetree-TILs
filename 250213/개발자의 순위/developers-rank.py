from itertools import combinations
from collections import defaultdict

k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

person_dict = defaultdict(int)


for a in arr:
    for i in combinations(a, 2):
        person_dict[i] += 1

answer = 0

for key, val in person_dict.items():
    if val == k:
        answer += 1

print(answer)