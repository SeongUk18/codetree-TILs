N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

# 가격 + 배송비 기준으로 정렬
gifts.sort(key=lambda x: x[0] + x[1])

max_people = 0

# 각 인원을 선택하는 경우를 최적화
for i in range(N):
    total_price = 0
    count = 0

    for j in range(N):
        price, delivery = gifts[j]
        
        # i번째 선물을 할인하는 경우
        if j == i:
            price //= 2  # 반값 할인 적용
        
        total_price += price + delivery

        # 예산 초과 시 중단
        if total_price > B:
            break

        count += 1
    
    max_people = max(max_people, count)

print(max_people)
