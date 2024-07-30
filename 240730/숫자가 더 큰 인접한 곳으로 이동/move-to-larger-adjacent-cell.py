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
    cur = map_list[r][c]
    for i in range(4):
        nx = r + x_list[i]
        ny = c + y_list[i]
        if 0 <= nx < n and 0 <= ny < n and map_check[nx][ny]:  
            cur_n = map_list[nx][ny]
            map_check[nx][ny] = False
            if cur <= cur_n:
                n_r, n_c = nx, ny
                break
                
    
    return n_r, n_c

num_list = [map_list[r][c]]
map_check[r][c] = False  

while True:
    r, c = serch(map_list, map_check, r, c)
    if num_list[-1] == map_list[r][c]: 
        break
    else:
        num_list.append(map_list[r][c])

for i in num_list:
    print(i, end= " ")