def max_gifts(N, B, gifts):
    # (가격 + 배송비 기준 정렬) → 작은 비용부터 고려
    gifts.sort(key=lambda x: x[0] + x[1])

    max_people = 0

    # (1) 하나의 선물을 할인했을 때, 최대 인원 탐색
    for i in range(N):
        discounted_price = gifts[i][0] // 2  # i번째 선물만 할인
        new_gifts = gifts[:]  # 원본 리스트 유지
        new_gifts[i] = (discounted_price, new_gifts[i][1])  # i번째 선물만 할인 적용

        new_gifts.sort(key=lambda x: x[0] + x[1])

        new_price = 0
        new_count = 0

        for price, delivery in new_gifts:
            new_price += price + delivery

            if new_price > B:
                break
            new_count += 1

        max_people = max(max_people, new_count)  

    return max_people


N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
print(max_gifts(N, B, gifts))
