
string = 'saaganada'
string_output = 'saagin'
count = 0
count_a = list(string).count('a')
print(count_a)
list_string = list(string)
"""
for i in list_string:
    if i == 'a':
        count = count + 1

    if count == 4 and i == 'a':
        print('hi')
        i = i.replace('a','!')
        print(i)
print(list_string)
"""
for i in range(0,len(list_string)):
    if list_string[i] == 'a':
        count = count + 1

    if count == 4 and list_string[i] == 'a':
        print('hi')
        list_string[i] = '!'

print(list_string)
string_new = ''.join(list_string)
print(string_new)







