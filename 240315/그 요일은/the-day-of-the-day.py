# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
weekday = input()

# 윤년의 각 월별 일수
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 총 일수 계산
total_days = d2
if m1 == m2:
    total_days = d2 - d1
else:
    total_days += days_in_month[m1] - d1
    for month in range(m1 + 1, m2):
        total_days += days_in_month[month]

# 특정 요일까지의 일수
target_index = weekdays.index(weekday)

# 전체 기간에 걸친 주 수
full_weeks = total_days // 7

# 추가 일수 계산
extra_days_start = 0
extra_days_end = (extra_days_start + total_days) % 7  # 종료 날짜 이후의 요일

# 발생 횟수 계산
occurrences = full_weeks
if extra_days_start <= target_index:
    if extra_days_end + 7 * full_weeks >= target_index:
        occurrences += 1
elif extra_days_start > target_index:
    if extra_days_end < extra_days_start:
        if target_index < extra_days_end or target_index >= extra_days_start:
            occurrences += 1

print(occurrences)