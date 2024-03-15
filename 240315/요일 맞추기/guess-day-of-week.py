m1, d1, m2, d2 = map(int, input().split())
elapsed_days = 0
day_of_the_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if m1 != m2:
    for i in range(m1, m2):
        if i == m1:
            elapsed_days += num_of_days[i] - d1
        else:
            elapsed_days += num_of_days[i]
    elapsed_days += d2
else:
    elapsed_days = d2 - d1

d_o_t_w = elapsed_days % 7
answer = d_o_t_w + 1
if answer >= 7:
    answer = answer % 7
print(day_of_the_week[answer])