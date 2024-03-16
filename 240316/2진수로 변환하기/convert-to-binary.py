n = int(input())

answer = []

while True:
    answer.append(n % 2)
    n = n // 2
    if n == 0 or n == 1:
        answer.append(n)
        break


for i in answer[::-1]:
    print(i, end="")