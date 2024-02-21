n, total = map(int, input().split())
money = []
count = 0
for _ in range(n):
    money.append(int(input()))

while money:
    coin = money.pop()
    count += total // coin
    total = total % coin
    if total == 0:
        break

print(count)