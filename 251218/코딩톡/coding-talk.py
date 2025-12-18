n, m, p = map(int, input().split())
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

people = [chr(i) for i in range(65, 65 + n)]

# p번째 메시지를 확실히 읽은 사람들
read_people = set()

# 1. p번째 메시지를 보낸 사람
read_people.add(c[p - 1])

# 2. p번째 이후 메시지를 보낸 사람
for i in range(p, m):
    read_people.add(c[i])

# 읽지 않았을 가능성이 있는 사람들 출력
for person in people:
    if person not in read_people:
        print(person, end=" ")
