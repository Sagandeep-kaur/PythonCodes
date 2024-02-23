string = 'aaaabbbccdddddddde'
dict = {}

for i in string:
    if i not in dict:
       dict[i] = 1

    else:
        dict[i] = dict[i] + 1
print(dict)

# insert commas between digits
string2 = '123890567'
list = string2.split()
list2 =[]
print(len(string2))
print(list)
for i in range(0,len(string2)):
    for j in string2[i]:

        list2.append(j)
        if i == len(string2) - 1:
           break
        list2.append(',')

print(list2)
string3 = ' '.join(list2)
print(string3)

string3 = '123890567'
list2 = [i for i in string3]
print(list2)
string3 =','.join(list2)
print(string3)





