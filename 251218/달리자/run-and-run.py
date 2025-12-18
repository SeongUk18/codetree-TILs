n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

run_people = 0
answer = 0

for i in range(n - 1):
    a = A[i] + run_people
    b = B[i]

    run_people = 0

    if a > b:
        run_people = a - b
        # print(run_people)
        answer += run_people

        

print(answer)