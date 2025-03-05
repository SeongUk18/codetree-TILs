from itertools import combinations

def max_arithmetic_sequences(arr):
    n = len(arr)
    max_count = 0
    
    for i, j in combinations(range(n), 2):
        ai, aj = arr[i], arr[j]
        if (ai + aj) % 2 != 0:
            continue 
        
        K = (ai + aj) // 2
        count = 0
        
        for x, y in combinations(range(n), 2):
            ax, ay = arr[x], arr[y]
            if (ax + ay) // 2 == K and (ax + ay) % 2 == 0:
                count += 1
        
        max_count = max(max_count, count)
    
    return max_count

N = int(input())
arr = list(map(int, input().split()))

print(max_arithmetic_sequences(arr))