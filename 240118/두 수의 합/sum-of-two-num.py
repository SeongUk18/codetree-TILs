# 조합으로 진행하려고 했으나, 시간 초과로 코드 변경
# from itertools import combinations

# n, m = map(int, input().split())

# numbers = list(map(int, input().split()))
# num = 0

# for i in combinations(numbers, 2):
#     if sum(i) == m:
#         num += 1

# print(num)

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 리스트 정렬
numbers.sort()
# 투 포인터 이용
left, right = 0, n - 1
num = 0
while left < right:
    # 두 수의 합 계산
    current_sum = numbers[left] + numbers[right]

    if current_sum == m:
        num += 1
        left += 1
        right -= 1
    elif current_sum < m:
        left += 1
    else:
        right -= 1

print(num)