# shift all zeros to right
list = [1,3,4,0,23,0,1,3,0,67,50,5,0,11]
k = 0
for i in list:
    # check whether a current element is non-zero
    # if not then store next free position in the list
    if i!=0:
        list[k] = i
        k = k + 1
#print(list)
print(k)
for i in range(k, len(list)):
    list[i] = 0
print(list)