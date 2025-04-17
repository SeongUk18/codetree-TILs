def min_total_cost(n, k, nums):
    nums.sort()
    min_cost = float('inf')

    for i in range(10001):  # 기준 숫자 범위 [i, i+k]
        lower = i
        upper = i + k
        total_cost = 0

        for num in nums:
            if lower <= num <= upper:
                continue  # 바꿀 필요 없음
            elif num < lower:
                total_cost += lower - num
            else:  # num > upper
                total_cost += num - upper

        min_cost = min(min_cost, total_cost)

    return min_cost

# 예시 입력
n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(min_total_cost(n, k, nums))
