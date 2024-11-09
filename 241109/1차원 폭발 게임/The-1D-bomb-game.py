n, m = map(int, input().split())

booms = {}

for i in range(n):
    booms[i] = int(input())


while True:
    prev = None
    count = 0
    find = []
    exploded = False

    for key, val in list(booms.items()):
        if prev == val:
            count += 1
            find.append(key)
        else:
            if count >= m:
                for idx in find:
                    del booms[idx]
                exploded = True

            count = 1
            prev = val
            find = [key]
    # 마지막 연속된거 확인    
    if count >= m:
        for idx in find:
            del booms[idx]
        exploded = True

    if not exploded:
        break

print(len(booms))
for val in booms.values():
    print(val)