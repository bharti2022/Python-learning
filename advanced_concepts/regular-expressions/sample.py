import re
text = 'abcdfghijk'
parser = re.search('a[b-f]*f', text)
print (parser)

print (parser.group())
#'abcdf'

#search pattern matching
string1 = "hello from bharti"
strings = ['hello', 'bharti']

for string in strings:
    match = re.search(string, string1)
    if match:
        print('found match')
        print(match)
    else:
        print('not found')    

silly_string = "the cat in the hat"
pattern = "the"
print (re.findall(pattern, silly_string))    

s1='\$'
print(re.search(s1,'abc\$'))
