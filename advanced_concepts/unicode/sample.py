# Python 3
x = 'blah'
print (type(x))

y = u'blah'
print (type(y) )

# print (('abcdef' + chr(255)).encode('utf-8'))
#b'abcdef\xc3\xbf'

#encode
encodes = "encode the string".encode(encoding='utf-8')

print(encodes)

#decode
print(encodes.decode('utf-8','strict'))



