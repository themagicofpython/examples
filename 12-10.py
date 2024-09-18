import socketserver
class RequestHandler(socketserver.StreamRequestHandler):
  def handle(self):
    l = True
    while l:
      l = self.rfile.readline().strip()
      if l:
        self.wfile.write(l[::-1] + '\n')
hostname = '127.0.0.1'
port = 3456	
server = socketserver.ThreadingTCPServer((hostname, port), RequestHandler)
server.serve_forever()
