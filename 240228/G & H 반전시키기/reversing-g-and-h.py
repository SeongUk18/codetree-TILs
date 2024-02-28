n = int(input())

s1 = input()
s2 = input()
before = False
cnt = 0

for i in range(n):
    if s1[i] != s2[i]:
        if before:
            continue
        else:
            before = True
            cnt += 1
    else:
        before = False
        continue

print(cnt)