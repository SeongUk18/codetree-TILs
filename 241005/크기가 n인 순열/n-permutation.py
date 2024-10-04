n = int(input())

used = [False for _ in range(n + 1)]
num_list = [x for x in range(1, n + 1)]

def backtracking(used, answer):
    if len(answer) == n:
        print(" ".join(map(str, answer)))

    for i in range(len(num_list)):
        if not used[i]:
            used[i] = True
            answer.append(num_list[i])
            backtracking(used, answer)
            used[i] = False
            answer.pop()

backtracking(used, [])