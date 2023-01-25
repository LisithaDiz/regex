import re

s = 'Lisitha @lisithaThenuka jc&kjs sxkja 56121asxkj5 dcsd22sdc dc{dcd Spain'

z = re.findall("Lisitha\Z", s)  # Checlk the ending word
print(z)

print(" w ")

z = re.findall("\w", s)
print(z)
z = re.findall("\W", s)
print(z)

print(" s ")

z = re.findall("\s", s)
print(z)
z = re.findall('\S', s)
print(z)

print(" d ")

z = re.findall("\d", s)
print(z)
z = re.findall("\D", s)
print(z)

print(" b ")
z = re.findall("\b", s)
print(z)
z = re.findall("\B", s)
print(z)

'''s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
print(s)
lst = re.findall('\S+@\S+', s)
print(lst)'''

o = "My3kjn 45 kjsd55dv"
l = re.findall('\S+[0-9]\S+', o) #\S+[0-9]\S+
print(l)

xx = "From: Using the : character"
y = re.findall("^F.+?", xx)
print(y)

c ="$sdf"
yy = re.findall('\$', c)
print(yy)