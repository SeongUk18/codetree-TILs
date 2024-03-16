n = int(input())

answer = []

while n > 0:
    answer.append(n % 2)
    n = n // 2

for i in answer[::-1]:
    print(i, end="")