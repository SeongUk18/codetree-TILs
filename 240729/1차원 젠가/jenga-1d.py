n = int(input())

tower = []

for _ in range(n):
    tower.append(int(input()))

for _ in range(2):
    s, e = map(int, input().split())

    tower = tower[:s - 1] + tower[e:]


print(len(tower))
for t in tower:
    print(t)