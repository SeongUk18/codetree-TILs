from collections import defaultdict

n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

count_dict = defaultdict(int)

for a, b in pairs:
    if (a, b) in count_dict or (b, a) in count_dict:
        count_dict[(a, b)] += 1
        count_dict[(b, a)] += 1
 
    else:
        count_dict[(a, b)] = 1
        count_dict[(b, a)] = 1


# print(count_dict)
print(max(list(count_dict.values())))