import socket
s = socket.socket()
host = '127.0.0.1'
port = 1234
s.connect((host, port))
task = input("enter a task: ")
s.send(str.encode(task))
print("=====tasks=====")
full_reply = bytearray("", "UTF-8")
reply = s.recv(10)
full_reply += reply
while reply:
	reply = s.recv(10)
	full_reply += reply
print(full_reply)
