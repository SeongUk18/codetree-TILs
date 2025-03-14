N = int(input())
str = input()

def find(N, str):
    for i in range(1, N):
        if all(str[j:j + i] not in str[j + i:] for j in range(N - i)):
            return i
                   

            

print(find(N, str))