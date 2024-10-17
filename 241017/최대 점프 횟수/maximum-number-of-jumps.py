n = int(input())
n_list = list(map(int, input().split()))

# dp[i]는 i번째 위치까지 도달하는 데 필요한 최대 점프 횟수
dp = [-1] * n  # -1로 초기화 (방문하지 않은 위치)
dp[0] = 0  # 시작점은 0번 점프한 상태

# 각 위치에서 점프 가능한 범위 탐색
for i in range(n):
    if dp[i] == -1:  # 아직 도달하지 못한 곳은 건너뜀
        continue
    for j in range(1, n_list[i] + 1):
        if i + j < n:
            dp[i + j] = max(dp[i + j], dp[i] + 1)  # 점프 횟수를 갱신

# dp 배열에서 가장 큰 값이 최대 점프 횟수
print(max(dp))