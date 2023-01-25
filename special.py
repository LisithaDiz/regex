import re

text = "The 8 rain  58 in  the Spain 52"

x = re.findall("[A-z1-5]", text)  # FindAll charncter between A to z
print(x)

x = re.findall("\d", text)  # FindAll digits
print(x)

x = re.findall("r..n", text)
print(x)

x = re.findall("^The", text)
print(x)
if x:
    print("Yes, the string starts with 'The'")
else:
    print("No match")

x = re.findall("52$", text)
print(x)
if x:
    print("Yes, the string ends with '52'")
else:
    print("No match")