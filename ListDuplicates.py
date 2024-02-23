list_one = [1,1,2,3,4,8,7,1,2,8,9,3,3,3,1,2]
list_two = []
dupList =[]
count = 0
for i in list_one:
    if i not in list_two:
        list_two.append(i)

    elif i in list_two and i not in dupList:
        dupList.append(i)
print(list_two)
print(dupList)
'''
for i in range(0,len(list_one)):
    
     if list_one[i] not in list_two:
        list_two.append(list_one[i])

     else:
         dupList.append(list_one[i])
'''
#print(dupList)
dupset = set(dupList)
# count the duplicate elements
print("count is", len(dupset))
print(list_two)

# remove duplicates from list quickly
list_one = set(list_one)
print(list_one)



list_One = [1,1,2,3,4,8,7,1,2,8,9,3,3]
#using dictionary - find the count of each element in the list
dict_one ={}

for i in list_One:
    if i in dict_one:
       dict_one[i] = dict_one[i] + 1
    else:
        dict_one[i] = 1

print(dict_one)