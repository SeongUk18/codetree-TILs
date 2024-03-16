n = int(input())

answer = []

while True:
    if n == 0 or n == 1:
        answer.append(n)
        break
    answer.append(n % 2)
    n = n // 2
    


for i in answer[::-1]:
    print(i, end="")