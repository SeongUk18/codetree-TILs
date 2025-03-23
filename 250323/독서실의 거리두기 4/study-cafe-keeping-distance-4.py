N = int(input())
seat = list(input())

max_dist = float('-inf')

for i in range(N):
    if seat[i] == "0":
        new_seat = seat[::]
        new_seat[i] = "1"
        for j in range(N):
            if new_seat[j] == "0":
                n_new_seat = new_seat[::]
                n_new_seat[j] = "1"
                seat_count = []
                for k in range(N):
                    if n_new_seat[k] == "1":
                        seat_count.append(k)

                min_dist = float('inf')
                for k in range(1, len(seat_count)):
                    dist = seat_count[k] - seat_count[k - 1]
                    min_dist = min(dist, min_dist)

                max_dist = max(min_dist, max_dist)

print(max_dist)