N = int(input())
seat = input()

max_dist = float('-inf')
seat = list(seat)

for i in range(N):
    if seat[i] == "0":
        new_seat = seat.copy()
        new_seat[i] = "1"
        seat_list = []
        # print(new_seat)
        min_dist = float('inf')
        for j in range(N):
            if new_seat[j] == "1":
                seat_list.append(j)
        start = seat_list[0]
        # print(seat_list)
        for s in seat_list[1:]:
            diff = s - start
            start = s
            min_dist = min(min_dist, diff)
        max_dist = max(max_dist, min_dist)
print(max_dist)