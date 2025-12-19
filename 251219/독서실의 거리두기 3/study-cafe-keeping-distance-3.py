N = int(input())
seats = list(input())

# Please write your code here.
max_dist = float('-inf')

for i in range(N):
    if seats[i] == "0":
        seats[i] = "1"
        dist = 0
        for j in range(N):
            if seats[j] == "1":
                dist += 1
            else:
                max_dist = max(dist, max_dist)
                dist = 0
        seats[i] = "0"

print(max_dist)