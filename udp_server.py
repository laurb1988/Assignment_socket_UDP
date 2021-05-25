import socket
import time
import datetime
server_port = 21060
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', server_port))
print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))
while True:
    message, address = server_socket.recvfrom(65535)
    client_time = message.split(b"|")[0]
    #Time Method
    #time_dif = time.time() - float(client_time)
    #Datetime Method
    decoded_time = client_time.decode('utf8')
    time_from_client = datetime.datetime.strptime(str(decoded_time), '%Y:%m:%d:%H:%M:%S')
    time_diff = (datetime.datetime.now() - time_from_client).total_seconds() / 60
    modified_message = 'Time: ' + str(time_diff) + ' seconds Message: Hello Client!'
    print ('[SERVER] The client at {}, originally sent: {}'.format(address, repr(message)))
    server_socket.sendto(bytes('Server is sending back: "{}".'.format(modified_message), encoding='utf8'), address)
server_socket.close()
