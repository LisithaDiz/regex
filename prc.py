import re

hand = open('lisitha1234.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    s = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(s) != 1: continue
    num = float(s[0])
    numlist.append(num)
print("max", max(numlist))
