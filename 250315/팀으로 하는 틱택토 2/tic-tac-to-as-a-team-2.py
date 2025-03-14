inp = [input() for _ in range(3)]

N = 3
answer = set()

for i in range(N):
    team_set = set()
    for j in range(N):
        team_set.add(inp[i][j])
    # print(team_set)
    if len(team_set) == 2:
        # print(team_set)
        answer.add(tuple(team_set))

for i in range(N):
    team_set = set()
    for j in range(N):
        team_set.add(inp[j][i])
    # print(team_set)    
    if len(team_set) == 2:
        # print(team_set)
        answer.add(tuple(team_set))

team_set = set()
for i in range(N):
    team_set.add(inp[i][i])
# print(team_set)
if len(team_set) == 2:
    # print(team_set)
    answer.add(tuple(team_set))

team_set = set()
for i in range(N):
    team_set.add(inp[2 - i][i])
# print(team_set)
if len(team_set) == 2:
    # print(team_set)
    answer.add(tuple(team_set))


print(len(answer))