from itertools import combinations

arr = list(map(int, input().split()))

min_diff = float('inf')
abil_dict = {}

for comb in combinations(arr, 2):
    other = [a for a in arr if a not in comb]

    for comb2 in combinations(other, 2):
        last = [a for a in other if a not in comb2]
        # print(comb, comb2, last)
        diff = max(sum(comb), sum(comb2), sum(last)) - min(sum(comb), sum(comb2), sum(last))
        # print(diff)
        if diff == 0:
            continue
        min_diff = min(diff, min_diff)
        abil_dict[min_diff] = [sum(comb), sum(comb2), sum(last)]

# print(abil_dict)
if min_diff == float('inf') or abil_dict[min_diff][0] == abil_dict[min_diff][1] == abil_dict[min_diff][2]:
    print(-1)
else:
    print(min_diff) 