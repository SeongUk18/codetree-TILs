n = int(input())
c, s = [], []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))

# Please write your code here.
score_a = 0
score_b = 0
score_c = 0
answer = 0

winner = 'ABC'
victory = 'ABC'

for i in range(n):
    if c[i] == "A":
        score_a += s[i]
    elif c[i] == "B":
        score_b += s[i]
    else:
        score_c += s[i]

    if score_a == score_b == score_c:
        winner = 'ABC'
    elif score_a > score_b and score_a > score_c:
        winner = 'A'
    elif score_b > score_a and score_b >score_c:
        winner = 'B'
    elif score_c > score_a and score_c > score_b:
        winner = 'C'
    elif score_a > score_b and score_a == score_c:
        winner = 'AC'
    elif score_a > score_c and score_a == score_b:
        winner = 'AB'
    elif score_b > score_a and score_b == score_c:
        winner = 'BC'

    if winner != victory:
        victory = winner
        answer += 1

print(answer)