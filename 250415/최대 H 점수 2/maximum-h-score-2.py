from itertools import combinations

def calc_h_score(arr):
    # H-점수 계산 함수
    for h in range(100, 0, -1):
        count = sum(1 for x in arr if x >= h)
        if count >= h:
            return h
    return 0

def solve(n, l, nums):
    max_h = 0
    indices = list(range(n))
    
    # 모든 경우의 수 중에서 최대 L개의 인덱스를 선택해 값을 +1
    for cnt in range(l+1):
        for comb in combinations(indices, cnt):
            temp = nums[:]
            for i in comb:
                temp[i] += 1
            h_score = calc_h_score(temp)
            max_h = max(max_h, h_score)
    
    return max_h

# 입력 예시
n, l = map(int, input().split())
nums = list(map(int, input().split()))
print(solve(n, l, nums))
