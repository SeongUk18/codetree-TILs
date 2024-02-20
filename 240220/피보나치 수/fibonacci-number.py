n = int(input())
fibo_dic = {1:1, 2:1}

def fibo(number):
    if number in fibo_dic:
        return fibo_dic[number]
    else:
        fibo_dic[number] = fibo(number - 1) + fibo(number - 2)
        return fibo_dic[number]

print(fibo(n))