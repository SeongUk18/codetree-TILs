from collections import defaultdict

N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_dict = defaultdict(int)
for _ in range(S):
    person, time = map(int, input().split())
    sick_dict[person] = time

milk_dict = defaultdict(list)

for i in range(D):
    milk_dict[m[i]].append((p[i], t[i]))

# print(milk_dict)
# print(sick_dict)

max_person = float('-inf')

for key, val in milk_dict.items():
    if all(person in sick_dict or time > sick_dict[person] for person, time in val):
        max_person = max(max_person, len(val))

print(max_person)