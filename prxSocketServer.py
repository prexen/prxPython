


import socketserver
import socket
import signal # Allow socket destruction on Ctrl+C
import sys
import time
import threading
import json


def _handle_client(client, address):
    """
    Main loop for handling connecting clients and serving files from content_dir
    Parameters:
        - client: socket client from accept()
        - address: socket address from accept()
    """
    PACKET_SIZE = 1024
    while True:
        print("CLIENT", client)
        
        data = client.recv(PACKET_SIZE).decode() # Recieve data packet from client and decode
        if(not data):
            break
        request_method = data.split(' ')[0]
        print("Method: {m}".format(m=request_method))
        print("Request Body: {b}".format(b=data))
        print("Path: {p}".format(p=data.split(' ')[1]))


        #"Content-Type: application/json"
        if (request_method == "GET"):
            
            #Aprender a parsear o query!!!

            #mydata = {"name": "Apple", "quantity": 42, "date": "2014-02-27" }
            #serializeddata = json.dumps(mydata)
            headerCode = '\HTTP/1.1 200 OK\n'
            headerContent = ('Content-Type: text/html\n')
            time_now = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
            headerDate = 'Date: {now}\n'.format(now=time_now)

            #char *hello = "HTTP/1.1 200 OK\nContent-Type: text/plain\nContent-Length: 12\n\nHello world!";

            resposeHeader = headerCode
            resposeHeader += headerContent
            resposeHeader += headerDate
            resposeHeader += "\n"
            
            response = resposeHeader
                        
            response_data = "<html><body><p>Hello World via code!</p></body></html>"
            response += response_data

            http_response = """\
HTTP/1.1 200 OK
Content-Type: text/html
Date: 27/2/34

<html><body><p>Escrito tudo junto</p></body></html>
"""
            
            client.send(response.encode())
            client.close()
            print("Worked")
            break
                        
        else:
            print("Unknown HTTP request method: {method}".format(method=request_method))


HOST = "localhost"
PORT = 8000

#socket.SOCK_STREAM indicates TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(5)#par eh number of connections que o ele aceita
print("Server starting")
print("serving at", HOST)
print("serving at port", PORT)     

#FORKING PROCESSES --> cria um novo processo
#THREADS --> cria um thread novo no mesmo processo, mas pode dar merda de synch
#ASYNCHRONOUS I/O --> basicamente eh uma queue... #import asyncio
# como o webdriver do selenium so pode um por vez, vai ser asynch esse server...

while True:
    try:
        (client, address) = serversocket.accept()
        client.settimeout(60)
        print("Recieved connection from {addr}".format(addr=address))
        threading.Thread(target=_handle_client, args=(client, address)).start()
    except KeyboardInterrupt:
        print("Ending serve socket")
        serversocket.close()