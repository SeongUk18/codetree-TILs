n = int(input())

used = [False for _ in range(n + 1)]

def backtracking(answer, used):
    if len(answer) == n:
        print(" ".join(map(str, answer)))
        return

    for i in range(n, 0, -1):
        if not used[i]:
            # print(answer)
            used[i] = True
            answer.append(i)
            backtracking(answer, used)
            used[i] = False
            answer.pop()

backtracking([], used)