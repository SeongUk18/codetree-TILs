from itertools import permutations  # 순서를 섞어주는 도구

N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]
a, b = zip(*moves)
a, b = list(a), list(b)

# 바위(1)는 가위(0)를 이김 / 보(2)는 바위(1)를 이김 / 가위(0)는 보(2)를 이김
def check_win(p1, p2):
    if (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1) or (p1 == 0 and p2 == 2):
        return True
    return False

max_wins = 0

# 1, 2, 3번에 '가위, 바위, 보' 역할을 하나씩 배정하는 모든 경우(6가지)를 반복
for case in permutations([0, 1, 2]):    
    current_wins = 0
    for i in range(N):
        # 이번 판에서 두 사람이 낸 숫자를 실제 역할(0, 1, 2)로 변환
        p1_role = case[a[i] - 1] 
        p2_role = case[b[i] - 1]
        
        # 첫 번째 사람이 이겼는지 확인
        if check_win(p1_role, p2_role):
            current_wins += 1
            
    # 여태까지의 최고 승리 횟수와 비교해서 더 큰 값을 저장
    if current_wins > max_wins:
        max_wins = current_wins

print(max_wins)