import string
s = "The leet hackers!"
s = s.translate(str.maketrans("elta","3174"))
print(s)
s = "string. With. Punctuation?" # Sample string 
out = s.translate(str.maketrans("","",string.punctuation))
print(out)
