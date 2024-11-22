import heapq

# 입력
n = int(input())
num_list = list(map(int, input().split()))

# 누적 합 계산
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + num_list[i]

max_avg = 0

# K를 1부터 N-2까지 순회
for K in range(1, n - 1):
    # 남은 숫자 리스트 생성
    remaining_nums = num_list[K:]

    # 힙으로 변환 (O(N - K))
    heapq.heapify(remaining_nums)

    # 가장 작은 값 제거
    smallest = heapq.heappop(remaining_nums)

    # 남아있는 합 계산
    total_sum = prefix_sum[n] - prefix_sum[K] - smallest

    # 남아있는 숫자의 평균 계산
    remaining_count = n - K - 1
    current_avg = total_sum / remaining_count

    # 최대 평균 갱신
    max_avg = max(max_avg, current_avg)

print(f"{max_avg:.2f}")
