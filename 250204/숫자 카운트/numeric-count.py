from itertools import permutations

def count_valid_numbers(n, queries):
    possible_numbers = list(permutations(range(1, 10), 3)) 
    valid_count = 0

    for num in possible_numbers:
        valid = True
        for question, cnt1, cnt2 in queries:
            q_digits = [int(d) for d in str(question)]  
            num_digits = list(num)  
            
            strike = sum(num_digits[i] == q_digits[i] for i in range(3))
            ball = sum((num_digits[i] in q_digits) and (num_digits[i] != q_digits[i]) for i in range(3))
            
            if strike != cnt1 or ball != cnt2:
                valid = False
                break
        
        if valid:
            valid_count += 1

    return valid_count

# 입력 받기
n = int(input())
queries = [tuple(map(int, input().split())) for _ in range(n)]

# 가능한 수의 개수 출력
print(count_valid_numbers(n, queries))
