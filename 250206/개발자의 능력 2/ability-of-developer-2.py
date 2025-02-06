from itertools import combinations

ability = list(map(int, input().split()))

min_diff = float('inf')
for comb in combinations(ability, 2):
    other = [a for a in ability if a not in comb]
    for comb2 in combinations(other, 2):
        last = [a for a in other if a not in comb2]
        # print(comb, comb2, last)
        diff = max(sum(comb), sum(comb2), sum(last)) - min(sum(comb), sum(comb2), sum(last))
        min_diff = min(diff, min_diff)
print(min_diff)