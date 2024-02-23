a = 'silent'
b = 'nliets'
dict = {}

for k1, k2 in zip(a,b):
    if k1 not in dict:
        dict[k1] = 1
    else:
        dict[k1] = dict[k1] + 1
    if k2 not in dict:
       dict[k2]  = -1

    else:
        dict[k2] = dict[k2] - 1
print(dict)
for values in dict.values():
    if values !=0:
        print(its not )
