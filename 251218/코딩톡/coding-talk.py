n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

people = [chr(i) for i in range(65, 65 + n)]
# print(people)

# Please write your code here.
read_people = set()
for i in range(p - 1, m):
    read_people.add(c[i])

if p >= 2 and u[p - 1] == u[p - 2]:
    read_people.add(c[p - 2])

for i in read_people:
    people.remove(i)

# print(people)
for p in people:
    print(p, end=" ")