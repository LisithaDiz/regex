import re

txt = "Hello planet"
x = re.findall("He.*p", txt)
y = re.findall("He.*", txt)
z = re.findall("He.*o", txt)
a = re.findall("He.*l", txt)

print(x, y, z, a)

x = re.findall("He.+p", txt)
y = re.findall("He.+tyr", txt)
z = re.findall("He.+psdfsd", txt)
a = re.findall("He.+l", txt)

print(x, y, z, a)

x = re.findall("He.{4}p", txt)
print(x)

x = re.findall("H|sg", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
