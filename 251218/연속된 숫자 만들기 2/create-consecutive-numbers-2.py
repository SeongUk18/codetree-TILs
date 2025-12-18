pos = list(map(int, input().split()))

pos.sort()

first_dist = abs(pos[0] - pos[1]) 
second_dist = abs(pos[1] - pos[2])

if first_dist == second_dist == 1:
    print(0)
elif first_dist == 2 or second_dist == 2:
    print(1)
else:
    print(2)