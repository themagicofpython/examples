import smtplib
import string
from os.path import basename
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class gmailSender:
	def __init__(self, user, passw):
		self.s = smtplib.SMTP('smtp.gmail.com',587)
		self.s.ehlo()
		self.s.starttls()
		self.s.ehlo
		self.s.login(user, passw)
		
	def send_via_gmail(self, subject, to, sender, filepath, msgtxt):
			msg = MIMEMultipart()
			me = sender
			recipients = to
			msg['Subject'] = subject
			msg['From'] = sender
			msg['To'] = recipients
			msg.attach(MIMEText(msgtxt))
			if filepath:
				for f in filepath or []:
					with open(f, 'rb') as fil:
						part = MIMEApplication(fil.read(), Name=basename(f))
					part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
					msg.attach(part)
			self.s.sendmail(me, recipients, msg.as_string())
	
	def close(self):
		self.s.quit()


gmail = gmailSender('demercel','amaril78')
gmail.send_via_gmail('subject','vonodna@yahoo.com', 'demercel@gmail.com', '','test')
