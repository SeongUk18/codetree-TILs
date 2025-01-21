a = input()

a_list = list(a)

if '0' in a_list:
    for i in range(len(a_list)):
        if a_list[i] == '0':
            a_list[i] = '1'
            break
else:
    a_list[-1] = '0'

x = 1
num = 0
for i in range(len(a_list) - 1, -1, -1):
    number = int(a_list[i])
    num += x * number
    x *= 2

print(num)