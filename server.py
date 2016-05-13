# _*_ coding utf-8 _*_
"""Echo Server file."""
from __future__ import unicode_literals
import socket
import email.utils


def response_ok():
    """Return a "200 OK" message to the client."""
    status_code = u'HTTP/1.1 200 OK'
    content_type = u'Content-Type: text/plain; charset=utf-8'
    date = u'Date: ' + email.utils.formatdate(usegmt=True)
    space = u''
    body = u'Hello World'
    bytes_ = body.encode('utf-8')
    length = u'Content-Length: {}'.format(len(bytes_))
    full_response = [status_code, content_type, date, length, space, body]
    full_response = '\r\n'.join(full_response)
    return full_response


def response_error():
    """Return a "500" Error message to client."""
    status_code = u'HTTP/1.1 500 Internal Server Error'
    content_type = u'Content-Type: text/plain; charset=utf-8'
    date = u'Date: ' + email.utils.formatdate(usegmt=True)
    space = u''
    body = u'Server Error'
    bytes_ = body.encode('utf-8')
    length = u'Content-Length: {}'.format(len(bytes_))
    full_response = [status_code, content_type, date, length, space, body]
    full_response = '\r\n'.join(full_response)
    return full_response


def server():
    """Echo server functionality."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    while True:
        server.listen(1)
        conn, addr = server.accept()
        try:
                try:
                    buffer_length = 8
                    response_complete = False
                    message = ""
                    while not response_complete:
                        part = conn.recv(buffer_length)
                        message = message + part
                        message = message.decode('utf-8')
                        if len(part) < buffer_length:
                            response_complete = True
                    print(message)
                    conn.sendall(response_ok())
                    break
                except SystemError('Request Failed'):
                    conn.sendall(response_error())
                    break
        except KeyboardInterrupt:
            conn.close()
        finally:
            server.close()

if __name__ == '__main__':
    server()
