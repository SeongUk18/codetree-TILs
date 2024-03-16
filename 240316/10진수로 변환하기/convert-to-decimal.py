n = input()

answer = 0
x = 1
for i in n[::-1]:
    i = int(i)
    answer = i * x + answer
    x = x * 2
print(answer)