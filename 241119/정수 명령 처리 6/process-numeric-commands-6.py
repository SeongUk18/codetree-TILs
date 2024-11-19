import heapq

n = int(input())  

heap = []  

for _ in range(n):
    command = input().strip()
    if command == "pop":
        print(-heapq.heappop(heap))  # 음수로 저장된 값을 다시 양수로 변환하여 출력

    elif command == "size":
        print(len(heap)) 

    elif command == "empty":
        print(1 if not heap else 0)  # 힙이 비어 있으면 1, 아니면 0 출력

    elif command.startswith("push"):
        _, num = command.split()
        heapq.heappush(heap, -int(num))  # 음수로 변환하여 최대 힙 구현
        
    elif command == "top":
        print(-heap[0])  # 음수로 저장된 최댓값을 다시 양수로 변환하여 출력

