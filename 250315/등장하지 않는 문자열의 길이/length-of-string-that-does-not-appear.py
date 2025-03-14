N = int(input())
str = input()

def find(N, str):
    for i in range(N):

        for j in range(i, N):
            s = str[:i]

            if s not in str[i:]:
                return i
            

print(find(N, str))