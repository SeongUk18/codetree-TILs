from collections import deque

A = deque(list(input()))

# Please write your code here.
answer = float('inf')

def cal_length():
    start = A[0]
    count = 1
    str_word = ""

    for i in range(1, len(A)):
        if start == A[i]:
            count += 1
        else:
            str_word += str(start) + str(count)
            count = 1
            start = A[i]

    str_word += str(start) + str(count)

    return len(str_word)



for i in range(len(A)):
    answer = min(cal_length(), answer)
    x = A.pop()
    A.appendleft(x)

print(answer)