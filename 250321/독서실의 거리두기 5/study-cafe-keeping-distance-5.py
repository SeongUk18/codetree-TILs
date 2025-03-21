N = int(input())
seat = input()

max_dist = float('-inf')
seat = list(seat)

for i in range(N):
    if seat[i] == "0":
        new_seat = seat[:]
        front_seat = seat[:i]
        back_seat = seat[i + 1:]
        f_dist = 1
        b_dist = 1

        for j in range(len(front_seat) - 1, -1, -1):
            if front_seat[j] == "1":
                break
            else:
                f_dist += 1
        
        for j in range(len(back_seat)):
            if back_seat[j] == "1":
                break
            else:
                b_dist += 1

        if i == N - 1:
            b_dist = 20
        max_dist = max(max_dist, min(f_dist, b_dist))


print(max_dist)