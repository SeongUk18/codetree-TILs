n = int(input())
arr = [int(input()) for _ in range(n)]



def is_having_carry(a, b):
    # print(a, b)
    # 일의 자리
    first_a = a % 10
    first_b = b % 10
    # print(first_a, first_b)
    if first_a + first_b >= 10:
        return False

    # 십의 자리
    second_a = a % 100 // 10
    second_b = b % 100 // 10
    # print(second_a, second_b)
    if second_a + second_b >= 10:
        return False

    # 백의 자리
    third_a = a % 1000 // 100
    third_b = b % 1000 // 100
    # print(third_a, third_b)
    if third_a + third_b >= 10:
        return False

    # 천의 자리
    fourth_a = a % 10000 // 1000
    fourth_b = b % 10000 // 1000
    # print(fourth_a, fourth_b)
    if fourth_a + fourth_b >= 10:
        return False

    return True


max_num = float("-inf")

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if is_having_carry(arr[i], arr[j]):
            for k in range(n):
                if i == k or j == k:
                    continue
                if is_having_carry(arr[i] + arr[j], arr[k]):
                    max_num = max(max_num, arr[i] + arr[j] + arr[k])

if max_num > 0:
    print(max_num)
else:
    print(-1)


