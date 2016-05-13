# -*- coding: utf-8 -*-
"""Client module."""
from __future__ import unicode_literals
try:
   input = raw_input
except NameError:
   pass
import socket


def get_msg():
    """Ask user for message to send."""
    msg = input(u"What would you like to send? \n")
    return str(msg)


def client(message):
    """Send data to server."""
    addr_info = socket.getaddrinfo('127.0.0.1', 5001)
    stream_info = [i for i in addr_info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf-8'))
    client.shutdown(1)
    buffer_length = 64
    full_response = ""
    while True:
        part = client.recv(buffer_length)
        full_response = full_response + part.decode('utf-8')
        if len(part) < buffer_length:
            client.close()
            break
    print(full_response)
    return full_response

if __name__ == '__main__':
    message = get_msg()
    client(message)
