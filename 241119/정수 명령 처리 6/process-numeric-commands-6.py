import heapq

n = int(input())

heap = []

for _ in range(n):
    command = input()
    if command[:3] == "pop":
        print(heapq.heappop(heap))
    elif command[0] == "s":
        print(len(heap))
    elif command[0] == "e":
        if len(heap) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "p":
        comand, num = command.split()
        heapq.heappush(heap, int(num))
    elif command[0] == "t":
        print(heap[-1])