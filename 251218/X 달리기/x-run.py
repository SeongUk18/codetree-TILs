X = int(input())

# Please write your code here.
move = 0    # 이번에 이동할 거리 
current = 0 # 현재까지 온 거리
time = 0    # 걸린 시간

while current < X:
    move += 1  
    
    # 첫 번째 이동 (갈 때)
    current += move
    time += 1
    if current >= X: 
        break
        
    # 두 번째 이동 (멈출 때를 대비한 쌍둥이 이동)
    current += move
    time += 1
    if current >= X: 
        break

print(time)