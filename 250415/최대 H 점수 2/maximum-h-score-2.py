def is_possible(H, nums, L):
    cnt = 0
    for num in nums:
        if num >= H:
            cnt += 1
    if cnt >= H:
        return True

    # 나머지는 H - num == 1인 것만 골라야 함 (1씩만 증가 가능)
    needed = 0
    for num in nums:
        if num < H and num + 1 >= H:
            needed += 1
    return cnt + min(needed, L) >= H

def solve(n, l, nums):
    left, right = 0, 101
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid, nums, l):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# 입력 처리
n, l = map(int, input().split())
nums = list(map(int, input().split()))
print(solve(n, l, nums))
