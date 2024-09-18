key = 'TIGER'
text = 'ATTACKPEARLHARBOR'
s = ''
for i,c in enumerate(text):
	s += chr((ord(key[i % (len(key))]) ^ ord(text[i]))+65)
print(s)
s2 = ''
for i,c in enumerate(s):
	s2 += chr((ord(key[i % (len(key))]) ^ ord(s[i])-65))
print('>>>',s2)
