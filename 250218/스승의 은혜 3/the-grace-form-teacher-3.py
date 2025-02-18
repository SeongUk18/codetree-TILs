from itertools import combinations

N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]

max_people = 0
for i in range(N, 0, -1):
    for people in combinations(gifts, i):
        people = list(people)
        people.sort()
        # print(people)
        total_price = 0
        for price, delivery in people[:-1]:
            total_price += price
            total_price += delivery

        if total_price <= B:
            max_people = max(max_people, i)
            break

print(max_people)