N = int(input())
seats = list(input())

# Please write your code here.
max_dist = float('-inf')

for i in range(N):
    if seats[i] == "0":
        seats[i] = "1"
        dists = []
        dist = 1
        for j in range(1, N):
            
            if seats[j] == "0":
                dist += 1
            else:
                dists.append(dist)
                dist = 1
        # print(dists)
        max_dist = max(max_dist, min(dists))
        seats[i] = "0"

print(max_dist)