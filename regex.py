import re
# starts with a and ends with d
string = 'adbd tyui 12fr 909 ab abbb asdab d'
string2 = 'aghjid drtyuad'
# starts with a and ends with d
list =re.findall("^a.+d$", string2)
print(list)


#if string.startswith('adbd') and string.endswith('ab'):
    #print('found')
txt = "The rain  in Spain"
list =re.findall('^The.*Spain$', txt)
print(list)
x = re.search('^The.+Spain$', txt)
if x:
   print('found')
else:
   print('not found')
lie = 'Sp'
# check if the string ends with Spain
list =re.findall('^The.+Spain$', txt)
print(list)
string4 = 'wdd456 678'
list2 = re.findall('\d+', string4)
print(list2)


