s = "Was it a cat I saw?"

# Solution uses extra space proportional to size of string "s"
s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
print(s == s[::-1])