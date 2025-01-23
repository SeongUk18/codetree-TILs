n = int(input())
str = input()

answer = 0

for i in range(n - 2):
    if str[i] == "C":
        for j in range(i, n - 1):
            if str[j] == "O":
                for k in range(j, n):
                    if str[k] == "W":
                        answer += 1

print(answer)