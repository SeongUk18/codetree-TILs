N = int(input())
seat = input()

max_dist = float('-inf')
for i in range(N):
    if seat[i] == "0":
        front, back = 1, 1
        dist = 1
        for j in range(N):
            if j == 0:
                front = 20
            if j == N - 1:
                back = 20
            if j < i and seat[j] == "1":
                front = 1
            elif j < i and seat[j] == "0":
                front += 1
            elif j > i and seat[j] == "1":
                break
            elif j > i and seat[j] == "0":
                back += 1
        # print(i)
        # print(front, back, dist)
        dist = min(front, back)

        max_dist = max(max_dist, dist)

print(max_dist)