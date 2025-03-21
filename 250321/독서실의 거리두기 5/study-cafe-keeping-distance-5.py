N = int(input())
seat = input()

max_dist = float('-inf')
seat = list(seat)
# print(seat)
for i in range(N):
    if seat[i] == "0":
        new_seat = seat[:]
        new_seat[i] = "1"
        min_dist = float('inf')
        dist = 1
        dist_list = []
        # print(new_seat)
        for j in range(1, N):
            if j == N - 1:
                if new_seat[j] == "0":
                    dist += 1
                dist_list.append(dist)
            if new_seat[0] == "0":
                dist += 1

            if new_seat[j] == "1":
                # print(j, dist)
                dist_list.append(dist)
                dist = 1
            else:
                dist += 1
        # print(dist_list)
        max_dist = max(min(dist_list), max_dist)


print(max_dist)