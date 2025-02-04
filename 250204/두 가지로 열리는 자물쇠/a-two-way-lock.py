def is_near(x, y, N):
    return abs(x - y) <= 2 or abs(x - y) >= N - 2

def is_valid_combination(comb, ref, N):
    return all(is_near(comb[i], ref[i], N) for i in range(3))

def count_valid_combinations(N, first_comb, second_comb):
    count = 0

    for x in range(1, N+1):
        for y in range(1, N+1):
            for z in range(1, N+1):
                comb = (x, y, z)
                if is_valid_combination(comb, first_comb, N) or is_valid_combination(comb, second_comb, N):
                    count += 1

    return count

N = int(input().strip())
first_comb = tuple(map(int, input().split()))
second_comb = tuple(map(int, input().split()))

print(count_valid_combinations(N, first_comb, second_comb))
