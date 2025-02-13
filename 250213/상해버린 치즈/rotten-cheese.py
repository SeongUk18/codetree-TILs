from collections import defaultdict

N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_dict = defaultdict(int)
sick_p = []
for _ in range(S):
    person, time = map(int, input().split())
    sick_dict[person] = time
    sick_p.append(person)

milk_dict = defaultdict(list)
eat_mike = defaultdict(list)
for i in range(D):
    milk_dict[m[i]].append((p[i], t[i]))
    eat_mike[m[i]].append(p[i])

# print(milk_dict)
# print(sick_dict)

max_person = float('-inf')


for key, val in milk_dict.items():
    if all(s_p in eat_mike[key] for s_p in sick_p):
        if all(person in sick_dict or time > sick_dict[person] for person, time in val):
            max_person = max(max_person, len(val))

print(max_person)