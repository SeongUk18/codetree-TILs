N = int(input())

answer = 0
checkdict = dict()

for _ in range(N):
    num, pos = map(int, input().split())

    if num in checkdict:
        check = checkdict[num]

        if check == pos:
            continue
        else:
            checkdict[num] = pos
            answer += 1

    else:
        checkdict[num] = pos

print(answer)