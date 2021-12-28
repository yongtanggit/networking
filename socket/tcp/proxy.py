'''
pseudo code:
Create connections among server, proxy and client.
1. Server starts listening and waits for socket connection from proxy.
2. Proxy starts listening and waits for socket connection from client.
3. Client creates socket and connect with proxy.
4. Proxy creates a socket and connect with server.
5. Server receives connection from proxy.
communication
1. Client sends request to proxy.
2. Proxy handles the request and send the modified request to proxy.
3. Server accepts the request and send the response to proxy.
4. Proxy handles the response and send the modified response to client.


Functions:

receive
send
handler
display

'''

# listening and receive





