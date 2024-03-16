n, octal = map(int, input().split())

def changingOctal(n, octal):
    answer = []
    while True:
        if n < octal:
            answer.append(n)
            break
        answer.append(n % octal)
        n = n // octal
    return answer

answer = changingOctal(n, octal)

for i in answer[::-1]:
    print(i, end="")