A = input()
N = len(A)

answer = 0
for i in range(N - 3):
    if A[i] == "(" and A[i + 1] == "(":
        for j in range(i + 2, N - 1):
            if A[j] == ")" and A[j + 1] == ")":
                answer += 1

print(answer)