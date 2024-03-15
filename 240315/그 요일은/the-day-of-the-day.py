m1, d1, m2, d2 = map(int, input().split())
day_week = input()
elapsed_days = 0

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
index = day_of_the_week.index(day_week)

if m1 != m2:
    for i in range(m1, m2):
        if i == m1:
            elapsed_days += num_of_days[i] - d1 + 1
        else:
            elapsed_days += num_of_days[i]
    elapsed_days += d2
else:
    elapsed_days = d2 - d1 + 1

elapsed_days = elapsed_days - index
print(elapsed_days//7 + 1)