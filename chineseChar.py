import sys

f = open (sys.argv[1], 'r')
s = f.read()
count = 0
for c in s :
	if ord(c) > 0x4E00 and ord(c) < 0x9FFF:
		count += 1
print (count)