text = list(input())

t_dic = {}


for i in text:
    if i in t_dic:
        t_dic[i] += 1
    else:
        t_dic[i] = 1

n_dic = {v:k for k,v in t_dic.items()}

print(n_dic.get(1)[0])