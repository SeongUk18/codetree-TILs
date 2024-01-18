import sys

n = int(sys.stdin.readline())

dic = {}


def check_commend(commend):
    if commend[0] == "a":
        com, key, val = commend.split()
        dic[key] = val
    if commend[0] == "f":
        com, key = commend.split()
        if key in dic:
            print(dic[key])
        else:
            print("None")
    if commend[0] == "r":
        com, key = commend.split()
        del dic[key]
        
for _ in range(n):
    commend = sys.stdin.readline()
    check_commend(commend)