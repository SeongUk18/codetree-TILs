n = int(input())

def sol(n):
    if n == 0:
        return 1
    if n < 1:
        return 0
    
    return sol(n - 2) + sol(n - 3)

print(sol(n))