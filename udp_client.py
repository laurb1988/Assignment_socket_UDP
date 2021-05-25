import socket
import datetime
import time

server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Time Method
#input_s = str(time.time()) + '|Hello, Server!'
#Datetime method
timenow = datetime.datetime.now()
input_s =  timenow.strftime('%Y:%m:%d:%H:%M:%S') + '|Hello, Server!'
client_socket.sendto(bytes(input_s, encoding = 'utf8'), ('127.0.0.1', server_port))
input_s_modified, address = client_socket.recvfrom(65535)
print('[CLIENT] Response from server {}, is "{}"'.format(address, str(input_s_modified.decode('utf8'))))
client_socket.close()
