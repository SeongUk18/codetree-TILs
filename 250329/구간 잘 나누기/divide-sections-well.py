n, m = map(int, input().split())
a = list(map(int, input().split()))

def can_divide(arr, m, max_sum):
    count = 1
    curr_sum = 0
    for num in arr:
        if curr_sum + num > max_sum:
            count += 1
            curr_sum = num
        else:
            curr_sum += num
    return count <= m

def solve(N, M, arr):
    left = max(arr)
    right = sum(arr)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_divide(arr, M, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


print(solve(n, m, a))