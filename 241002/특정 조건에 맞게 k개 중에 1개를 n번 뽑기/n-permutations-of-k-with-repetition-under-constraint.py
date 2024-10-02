# 입력 받기
k, n = map(int, input().split())

num_list = [i for i in range(1, k + 1)]


answer_list = []

# 백트래킹용 함수 세팅
def backtracking(word_list):
    # 길이가 n인 순서쌍을 완성한 경우
    if len(word_list) == n:
        answer_list.append(word_list[:])  # 깊은 복사로 저장
        return 
    
    for i in num_list:
        # 연속으로 같은 숫자가 3번 이상 나오지 않도록 조건 체크
        if len(word_list) >= 2 and word_list[-2] == word_list[-1] == i:
            continue
        word_list.append(i)
        backtracking(word_list)  # 다음 단계로 백트래킹
        word_list.pop()  # 마지막 요소를 빼서 되돌림

backtracking([])

# 결과 출력
for comb in answer_list:
    print(' '.join(map(str, comb)))