from urllib.request import urlopen
webpage = urlopen('http://weather.sinoptik.bg/sofia-bulgaria-100727011?location').readlines()
for l in webpage:
	line = l.decode()

	if 'meta name="description" content="' in line:
		lft = line.find('Current weather')
		rght = line.find('Detailed')
		weather = line[lft:rght]
		print(weather)
		break
