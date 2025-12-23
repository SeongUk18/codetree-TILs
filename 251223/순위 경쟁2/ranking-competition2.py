n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
score_A = 0
score_B = 0
victory = 'AB'
answer = 0
winner = 'AB'

for i in range(n):
    if c[i] == 'A':
        score_A += s[i]
    else:
        score_B += s[i]

    if score_A == score_B:
        winner = 'AB'
    elif score_A > score_B:
        winner = 'A'
    else:
        winner = 'B'

    if victory != winner:
        victory = winner
        answer += 1

print(answer)