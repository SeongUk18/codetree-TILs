n = int(input())

numbers = list(map(int, input().split()))

sum_number = 0
answer = min(numbers)
for i in numbers:
    if sum_number < 0:
        sum_number = i
    else:
        sum_number += i
    answer = max(answer,sum_number)
print(answer)