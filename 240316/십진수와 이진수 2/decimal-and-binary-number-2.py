n = input()

x = 1
number = 0
answer = []

for i in n[::-1]:
    i = int(i)
    number += i * x
    x *= 2
number = number * 17

while True:
    if number < 2:
        answer.append(number)
        break
    answer.append(number % 2)
    number = number // 2

for i in answer[::-1]:
    print(i, end="")