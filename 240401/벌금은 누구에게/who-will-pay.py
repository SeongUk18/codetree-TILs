n, m, k = map(int, input().split())

def answer(n, m, k):
    student_list = [0 for _ in range(n + 1)]
    for _ in range(m):
        number = int(input())
        student_list[number] += 1
        if student_list[number] == k:
            return number
    return -1

print(answer(n, m, k))