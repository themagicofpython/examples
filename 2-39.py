txt = "Cheap xxx pictures and xxx videos! Quality mature xxx content! Get your xxx pass now!"
text = txt.split(' ')
for index,string in enumerate(text):
	if 'xxx' in string:
		text[index] = '[CENSORED]'
txt = " ".join(text)
print(txt)
