def count_weekday_occurrences(m1, d1, m2, d2, weekday):
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # 시작일부터 종료일까지 총 일수 계산
    total_days = sum(days_in_month[m1:m2]) + d2 - d1
    if m1 == m2:
        total_days = d2 - d1
    
    # 시작 요일부터 총 일수까지 특정 요일이 몇 번 발생하는지 계산
    start_weekday_index = (days_in_month[m1] - d1) % 7  # m1월 d1일의 요일 인덱스
    target_index = weekdays.index(weekday)

    # 전체 기간 동안 해당 요일이 발생하는 횟수 계산
    if occurrences < 7:
        return 0
    occurrences = total_days // 7  # 기본적으로 발생하는 주의 횟수
    if (start_weekday_index + total_days % 7) >= target_index:
        occurrences += 1

    return occurrences

# 입력
m1, d1, m2, d2 = map(int, input().split())
weekday = input()

# 계산 및 결과 출력
print(count_weekday_occurrences(m1, d1, m2, d2, weekday))