n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

people = [chr(i) for i in range(65, 65 + n)]
# print(people)

# Please write your code here.
if u[p - 1] == 0:
    print("")
    exit()

read_people = set()
for i in range(p - 1, m):
    read_people.add(c[i])


cnt = 1
while p - cnt - 1 >= 0:
    if u[p - cnt] == u[p - 1 - cnt]:
        read_people.add(c[p - cnt - 1])
        cnt += 1
    else:
        break
    

for i in read_people:
    people.remove(i)

# print(people)
if u[-1] == 0:
    print("")
else:
    for p in people:
        print(p, end=" ")