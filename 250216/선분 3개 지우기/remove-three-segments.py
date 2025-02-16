from itertools import combinations

n = int(input())
lines = []

for _ in range(n):
    left, right = map(int, input().split())
    lines.append((left, right))


answer = 0

for line in combinations(lines, len(lines) - 3):
    line_set = set()
    answer += 1
    for i in line:
        start, end = i
        if all(dot not in line_set for dot in range(start, end + 1)):
            # print(line_set)
            line_set = line_set.union(set(list(range(start, end + 1))))
        else:
            answer -= 1
            break
        
    

print(answer)