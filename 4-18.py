mails = {'Ivan':'vankata@abv.bg','Gergana':'hubavatageri@yahoo.com'}
print(mails.setdefault('Ivan'))
mails.setdefault('Joro')
print(mails)
mails.setdefault('Paco','N/A')
print(mails)
