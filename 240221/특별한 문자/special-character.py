text = list(input())

t_dic = {}


for i in text:
    if i in t_dic:
        t_dic[i] += 1
    else:
        t_dic[i] = 1

n_dic = {v:k for k,v in t_dic.items()}
t_index = list(t_dic.values())
t_keys = list(t_dic.keys())
index = t_index.index(1)
if index in t_keys:
    print(t_keys[index])
else:
    print("None")