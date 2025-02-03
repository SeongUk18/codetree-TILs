from itertools import combinations

abilities = list(map(int, input().split()))

min_diff = float('inf')
total_abil = sum(abilities)
for comb in combinations(abilities, 3):
    other = total_abil - sum(comb)
    min_diff = min(min_diff, abs(other - sum(comb)))

print(min_diff)