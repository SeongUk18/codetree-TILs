m1, d1, m2, d2 = map(int, input().split())
day_week = input()

# 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
index = day_of_the_week.index(day_week)

# 초기 날짜에서 요일의 인덱스 계산
start_day_index = (d1 - 1) % 7

# 경과 일수 계산
elapsed_days = 0
for i in range(m1, m2 + 1):
    if i == m1:
        elapsed_days += num_of_days[i] - d1
    elif i == m2:
        elapsed_days += d2
    else:
        elapsed_days += num_of_days[i]

# 시작 요일부터 계산하여, 해당 요일이 몇 번 등장하는지 계산
total_weeks, remaining_days = divmod(elapsed_days, 7)
day_count = total_weeks  # 해당 요일이 최소 등장하는 횟수

# 경과 일수를 기반으로 특정 요일이 추가로 등장하는지 확인
if remaining_days + start_day_index >= 7:
    day_count += 1

print(day_count)