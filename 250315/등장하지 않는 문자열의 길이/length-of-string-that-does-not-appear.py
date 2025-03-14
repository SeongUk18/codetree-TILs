N = int(input())
str = input()

def find(N, str):
    for i in range(1, N):
        if any(str[j:j + i] in str[j + 1:] for j in range(N)):
            continue
        else:
            return i
                   

            

print(find(N, str))