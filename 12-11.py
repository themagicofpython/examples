from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler
class Server(ThreadingMixIn, TCPServer): pass
class Handler(StreamRequestHandler):
   def handle(self):
      addr = self.request.getpeername()
      print('Got connection from', addr)
      self.wfile.write(b'Thank you for connecting')
server = Server(('', 12345), Handler)
server.serve_forever()
