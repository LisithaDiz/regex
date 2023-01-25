import re

txt = "From lisitha.thenuka@uct.ac.za Sat Jan  5 09:14:16 2008"
a = txt.find("@")
print(a)
b = txt.find(' ', a)
print(b)

print(txt[a + 1:b])

r = txt.split()
email = r[1]
print(email)
piece = email.split("@")
print(piece[1])

e = re.findall("^From .*@([^ ]*)", txt)
print(e)
