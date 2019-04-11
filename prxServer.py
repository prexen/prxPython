

import http.server
import socketserver
import io







#CGIHTTPRequestHandler

#myHandler.do_GET()
#http.server.SimpleHTTPRequestHandler(request, client_address, server, directory=None)
#http.server.CGIHTTPRequestHandler(request, client_address, server)
#http.server.HTTPServer(server_address, RequestHandlerClass)

class MyHandler(http.server.BaseHTTPRequestHandler):
    #def __init__(self, request, address, serverName):
        #print("self: ", self)
        #print("request: ", request)
        #print("address", address)
        #print("serverName", serverName)

        #pass
    
    '''
    def do_GET(self):
        self.send_response(200)
	    #self.send_header('Content-type','text/html')
	    #self.end_headers()
		# Send the html message
	    self.wfile.write("Hello World !")
	    return
    '''
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    #(self, c, a)
    #(self, clientRequest, clientAddress)
    def do_GET(self):
        #print(self.requestline)
        #print(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><head><title>Title goes here.</title></head>")
        self.wfile.write(b"<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write(b"</body></html>")
        self.wfile.close()
        #self.send_response("Hello World")
        

        '''
        request_data = self.request.recv(1024)
        print("o request:")
        print(''.join('< {line}\n'.format(line=line) for line in request_data.splitlines() ))
        request_line = request_data.splitlines()[0]
        request_line = request_line.rstrip('\r\n')

        print("depois das firula:")
        # Break down the request line into components
        request_method, path, request_version = request_line.split()
        print(request_method)
        print(path)
        print(request_version)

        #http_response = "Hello World"
        self.request.sendall("Hello World")
        self.request.close()
        '''


HOST = "localhost"
PORT = 8000
#myHandler = MyHandler
myServer = http.server.HTTPServer((HOST, PORT), MyHandler)
print(myServer.address_family)#tipo do socket...
print("serving at port", PORT)
print("queue req size: ", myServer.request_queue_size)
print("server address:", myServer.server_address)
print("----------------")
myServer.serve_forever()


'''    
while True:
    client_request, client_address = myServer.get_request()


request_data = client_request.recv(1024)
#client_connection, client_address = listen_socket.accept()
#request = client_connection.recv(1024)
#print (request_data)
#parse a request... #tenho q parsear a request pra saber 

print("o request:")
print(''.join('< {line}\n'.format(line=line) for line in request_data.splitlines() ))
    
request_line = request_data.splitlines()[0]
request_line = request_line.rstrip('\r\n')

print("depois das firula:")
# Break down the request line into components
request_method, path, request_version = request_line.split()
print(request_method)
print(path)
print(request_version)

#http_response = "Hello World"
#client_request.sendall(http_response)
client_request.close()
#client_connection.sendall(http_response)
#client_connection.close()
'''

'''
with http.server.HTTPServer((HOST, PORT), myHandler) as httpd:
    print(httpd.address_family)#tipo do socket...
    print("serving at port", PORT)
    print("queue req size: ", httpd.request_queue_size)
    
    httpd.serve_forever()
'''

'''
PORT = 8000
#Handler = http.server.SimpleHTTPRequestHandler
Handler = http.server.CGIHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

'''

