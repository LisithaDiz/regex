import re

hand = open("lisi.txt", "a")
hand.write("hi\n")
hand.write("hkuhadfjknsdsdi\n")
hand.write("hi From ohsefknff\n")
hand.write("hi kjhsd kughadland\n")
hand.write("hi lnjsdfnjc moijsd 65415\n")
hand.write("From fsdvsvsdvswsf\n")
hand.close()
hand = open("lisi.txt")
'''for line in hand:
    line = line.rstrip()
    if line.find("From") >= 0:
        print(line)

for line in hand:
    line = line.rstrip()
    if re.search("From", line):
        print(line)'''

'''for line in hand:
    if line.startswith('From'):
        print(line)'''

print("jhg")

for line in hand:
    if re.search("^From", line):
        print(line)