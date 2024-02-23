"""
string = 'i a1m 34rt rt 67 bn0 1 68 67'
count = 0
for i in string:
    if i in ('0,1,2,3,4,5,6,7,8,9'):
        count = count + 1

print(count)
"""
string = 'i a1m 34rt rt 67 bn0 1 68 67'
count = 0
for i in string:
    if i.isalpha():
        #print(i)
        count = count + 1

print(count)