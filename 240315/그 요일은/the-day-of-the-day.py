def calculate_occurrences(m1, d1, m2, d2, target_day):
    days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    total_days = d2 - d1
    for month in range(m1, m2):
        total_days += days_in_month[month]
    
    start_day = (sum(days_in_month[:m1]) + d1 - 1) % 7
    target_day_index = day_names.index(target_day)
    
    occurrences = 0
    for i in range(total_days + 1):
        if (start_day + i) % 7 == target_day_index:
            occurrences += 1

    return occurrences


m1, d1, m2, d2 = map(int, input().split())
day = input()


print(calculate_occurrences(m1, d1, m2, d2, day))