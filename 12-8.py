import socket
s = socket.socket()
host='127.0.0.1'
port = 1234
s.bind((host, port))
s.listen(5)
tasks = []
while True:
	c, addr = s.accept()
	print(addr, "connected")
	tasks.append(c.recv(1024))
	print(tasks)
	for task in tasks:
		c.send(task + str.encode(", "))
	c.close()
