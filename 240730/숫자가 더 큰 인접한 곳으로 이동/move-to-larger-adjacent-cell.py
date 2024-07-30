n, r, c = map(int, input().split())
r -= 1
c -= 1
map_list = []
map_check = [[True for _ in range(n)] for _ in range(n)]

x_list = [1, -1, 0, 0]
y_list = [0, 0, 1, -1]

for _ in range(n):
    map_list.append(list(map(int, input().split())))

def serch(map_list, map_check, r, c):
    n_r, n_c = r, c  
    cur = map_list[c][r]
    for i in range(4):
        nx = c + x_list[i]
        ny = r + y_list[i]
        if 0 <= nx < n and 0 <= ny < n and map_check[nx][ny]:  
            cur_n = map_list[nx][ny]
            map_check[nx][ny] = False
            if cur <= cur_n:
                n_c, n_r = nx, ny
                break
                
    
    return n_r, n_c

num_list = [map_list[c][r]]
map_check[c][r] = False  

while True:
    r, c = serch(map_list, map_check, r, c)
    if num_list[-1] == map_list[c][r]: 
        break
    else:
        num_list.append(map_list[c][r])

for i in num_list:
    print(i, end= " ")