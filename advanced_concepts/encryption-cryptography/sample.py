import hashlib
md5 = hashlib.md5()

md5.update(b'Python rocks!') #need byte string instead of regular string
print (md5.digest()) #digest method to get the hash code
