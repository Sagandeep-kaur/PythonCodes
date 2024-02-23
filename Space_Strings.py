str= 'i  am  a girl a     girl    '
#remove extra spaces from this string

str = str.replace('  ', ' ')
str = str.replace('   ', ' ')
print(str)
str= 'i  am  a girl a     girl123   345    ' \
     ''
# remove spaces using regex
import re
str_one = re.sub('\s+', ' ', str)
print(str_one)
List_one = re.findall('\s+', str)
print(List_one)

s = ' i am    a girl  yes uiop  '
print(s.split())
s = " $ ".join(s.split())
print(s)

# removing space using for loop
test_str = " GfG  is    good website   "
res = ""
print(len(test_str))
for i in range(len(test_str)):

    if (test_str[i] != " " or test_str[i-1] != " "):
       res = res + test_str[i]
print(res)
# using split and join function
stringg = ' my   name is       sugu'
stringg = stringg.split()
print(stringg)
stringg = ' '.join(stringg)
print(stringg)
